from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE_TYPE
import matplotlib.pyplot as plt
import os

# 슬라이드 키 → 레이아웃 이름 매핑
SLIDE_LAYOUT_MAP = {
    "cover_page": "Title Slide",
    "table_of_contents": "Title and Content",
    "project_understanding": "Title and Content",
    "client_needs_summary": "Title and Content",
    "market_analysis_market_overview": "Title and Content",
    "growth_trend_analysis": "Title and Content",
    "industry_drivers_challenges": "Title and Content",
    "competitive_benchmarking": "Title and Content",
    "swot_analysis": "Title and Content",
    "solution_overview": "Title and Content",
    "strategic_recommendations": "Title and Content",
    "implementation_plan": "Title and Content",
    "timeline_milestones": "Title and Content",
    "risk_management_plan": "Title and Content",
    "expected_benefits": "Title and Content",
    "investment_budget_estimation": "Title and Content",
    "team_introduction": "Title and Content",
    "why_us_differentiation": "Title and Content",
    "closing_summary": "Title and Content",
    "qna": "Title Only"
}

def create_presentation():
    return Presentation()

def get_layout_by_name(prs, layout_name):
    for layout in prs.slide_layouts:
        if layout.name == layout_name:
            return layout
    return prs.slide_layouts[0]  # fallback

def find_shape_by_type(slide, content_type="graph"):
    candidates = []
    for shape in slide.shapes:
        if shape.shape_type == MSO_SHAPE_TYPE.AUTO_SHAPE:
            if not shape.has_text_frame or not shape.text_frame.text.strip():
                candidates.append(shape)

    if not candidates:
        return None

    if content_type == "graph":
        return sorted(candidates, key=lambda s: (s.left + s.top))[0]
    elif content_type == "table":
        return sorted(candidates, key=lambda s: s.top)[-1]
    return None

def insert_graph(slide, data, placeholder_name="GraphLeft"):
    for shape in slide.shapes:
        if shape.name == placeholder_name and shape.shape_type == MSO_SHAPE_TYPE.AUTO_SHAPE:
            left, top, width, height = shape.left, shape.top, shape.width, shape.height
            break
    else:
        shape = find_shape_by_type(slide, "graph")
        if shape:
            left, top, width, height = shape.left, shape.top, shape.width, shape.height
        else:
            return  # 삽입 위치 없으면 생략

    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y'])
    ax.set_title(data.get('title', '그래프'))
    fig.savefig("temp_graph.png")
    plt.close(fig)
    slide.shapes.add_picture("temp_graph.png", left, top, width, height)
    os.remove("temp_graph.png")

def insert_table(slide, table_data, placeholder_name="TableMain"):
    rows = len(table_data)
    cols = len(table_data[0])
    for shape in slide.shapes:
        if shape.name == placeholder_name:
            left, top, width, height = shape.left, shape.top, shape.width, shape.height
            break
    else:
        shape = find_shape_by_type(slide, "table")
        if shape:
            left, top, width, height = shape.left, shape.top, shape.width, shape.height
        else:
            return  # 삽입 위치 없으면 생략

    table_shape = slide.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table
    for i in range(rows):
        for j in range(cols):
            table.cell(i, j).text = str(table_data[i][j])

def add_slide(prs, slide_key, slide_data):
    layout_name = SLIDE_LAYOUT_MAP.get(slide_key, "Title and Content")
    layout = get_layout_by_name(prs, layout_name)
    slide = prs.slides.add_slide(layout)

    title_shape = slide.shapes.title
    if title_shape and 'title' in slide_data:
        title_shape.text = slide_data['title']

    if 'text' in slide_data:
        for shape in slide.shapes:
            if not shape.is_placeholder:
                continue
            if "Content" in shape.name or "Text" in shape.name:
                shape.text = slide_data['text']
                break

    if 'graph' in slide_data:
        insert_graph(slide, slide_data['graph'])

    if 'table' in slide_data:
        insert_table(slide, slide_data['table'])

def generate_ppt(slides_content, output_path="generated_proposal.pptx"):
    prs = create_presentation()
    for slide_key, slide_data in slides_content.items():
        add_slide(prs, slide_key, slide_data)
    prs.save(output_path)
    return output_path

# 예시 실행용 데이터
slides_example = {
    "cover_page": {"title": "양자컴퓨팅 제안서", "text": "고객사: ABC Corp\n제출일: 2025.05.07"},
    "market_analysis_market_overview": {
        "title": "시장 개요",
        "text": "양자컴퓨팅 시장은 향후 5년간 고성장 예상.",
        "graph": {"x": [2021, 2022, 2023, 2024], "y": [1.2, 1.6, 2.3, 3.1], "title": "시장 규모 추이"}
    },
    "competitive_benchmarking": {
        "title": "경쟁사 비교 분석",
        "text": "주요 경쟁사 대비 당사의 차별점 정리.",
        "table": [
            ["업체명", "전략", "기술력"],
            ["Competitor A", "양자 HW", "우수"],
            ["Competitor B", "클라우드 중심", "보통"]
        ]
    }
}

# 테스트 실행
output_file_path = generate_ppt(slides_example)
output_file_path
