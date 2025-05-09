from input_handler import get_user_input
from rfp_analyzer import analyze_rfp
from slide_recommender import recommend_slides_llm
from research_question_generator import get_best_research_questions
from search_collector import search_serpapi
from research_answer_generator import summarize_research
from ppt_generator import generate_ppt_from_template

TEMPLATE_PATH = "customer_template.pptx"  # 고객 템플릿 경로
PLAN_TYPE = "advanced"  # or "basic"

def main():
    # 1. 사용자 입력
    user_inputs = get_user_input()

    # 2. RFP 분석
    rfp_result = analyze_rfp(user_inputs['rfp_text'], user_inputs['user_direction'])

    # 3. 슬라이드 추천
    recommended_slides = recommend_slides_llm(rfp_result['requirements'])

    # 4~6. 슬라이드별 리서치 질문 생성 + 검색 + 요약
    slide_contents = {}
    for slide_key in recommended_slides:
        questions = get_best_research_questions(
            slide_key, rfp_result['requirements'], plan_type=PLAN_TYPE
        )
        answers = []
        for q in questions:
            search_results = search_serpapi(q)
            summary = summarize_research(q, search_results)
            answers.append(summary)

        # 콘텐츠 생성 (지금은 간단화됨 → 나중에 GPT 통합 예정)
        slide_contents[slide_key] = {
            "title": slide_key.replace("_", " ").title(),
            "text": "\n".join(answers)
        }

    # 7. PPT 생성
    output_path = generate_ppt_from_template(recommended_slides, TEMPLATE_PATH, "final_output.pptx")

    print(f"\n✅ 제안서 생성 완료: {output_path}")

if __name__ == "__main__":
    main()
