import os
from input_handler import get_user_input
from rfp_analyzer import analyze_rfp
from slide_recommender import recommend_slides_llm
from research_question_generator import get_best_research_questions
from search_collector import search_serpapi
from research_answer_generator import summarize_research
from ppt_generator import generate_ppt_from_template

# 📁 경로 설정
TEMPLATE_DIR = "DB/ppt_template"
OUTPUT_DIR = "DB/proposal_result"
RFP_DIR = "DB/rfp"

PLAN_TYPE = "advanced"  # 또는 'basic'

def main():
    # 1. 사용자 입력 받기
    user_inputs = get_user_input()  # 여기에 RFP 텍스트, 방향성 등 포함

    # 2. RFP 요약 및 요구사항 추출
    rfp_result = analyze_rfp(user_inputs['rfp_text'], user_inputs['user_direction'])

    # 3. 슬라이드 추천
    recommended_slides = recommend_slides_llm(rfp_result['requirements'])

    # 4. 슬라이드별 질문 생성 + 검색 + 요약 정리
    slide_contents = {}
    for slide_key in recommended_slides:
        questions = get_best_research_questions(
            slide_key, rfp_result['requirements'], plan_type=PLAN_TYPE
        )
        answers = []
        for question in questions:
            search_results = search_serpapi(question)
            summary = summarize_research(question, search_results)
            answers.append(summary)

        slide_contents[slide_key] = {
            "title": slide_key.replace("_", " ").title(),
            "text": "\n".join(answers)
        }

    # 5. 템플릿 경로 가져오기
    template_files = os.listdir(TEMPLATE_DIR)
    if not template_files:
        raise FileNotFoundError("ppt_template 폴더에 템플릿 파일이 없습니다.")
    template_path = os.path.join(TEMPLATE_DIR, template_files[0])  # 첫 템플릿 사용

    # 6. 제안서 파일 이름 설정
    output_file = os.path.join(OUTPUT_DIR, "proposal_final.pptx")

    # 7. PPT 생성
    generate_ppt_from_template(list(slide_contents.keys()), template_path, output_file)
    print(f"\n✅ 제안서 생성 완료: {output_file}")

if __name__ == "__main__":
    main()
