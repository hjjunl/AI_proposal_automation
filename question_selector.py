# question_selector.py

from research_question_generator import generate_research_questions  # 고정 질문
from dynamic_question_generator import generate_dynamic_questions  # 동적 질문


def get_best_research_questions(slide_key, rfp_requirements, slide_templates, plan_type="basic"):
    """
    요금제에 따라 고정 질문 또는 GPT 기반 동적 질문을 선택해 반환한다.
    Args:
        slide_key (str): 슬라이드 키 이름
        rfp_requirements (list): 요구사항 리스트
        slide_templates (dict): 슬라이드 설명 템플릿
        plan_type (str): "basic" 또는 "advanced"

    Returns:
        list: 리서치 질문 리스트
    """
    if plan_type == "basic":
        return generate_research_questions(slide_key)

    elif plan_type == "advanced":
        static_qs = generate_research_questions(slide_key)
        dynamic_qs = generate_dynamic_questions(slide_key, rfp_requirements, slide_templates)

        # 간단한 비교 기준: 질문 길이 or 개수 기준
        if dynamic_qs and len(" ".join(dynamic_qs)) > len(" ".join(static_qs)):
            return dynamic_qs
        else:
            return static_qs

    else:
        raise ValueError("Invalid plan type: choose either 'basic' or 'advanced'")


# --- 테스트 예시 ---
if __name__ == "__main__":
    from slide_recommender import SLIDE_TEMPLATES

    test_slide = "solution_overview"
    rfp_requirements = [
        "기존 딥러닝 알고리즘을 양자컴퓨팅 기반으로 전환하여 성능 개선 방안 제시",
        "실제 양자 모델을 통해 적용 가능한 예시 및 결과 도출"
    ]

    print("\n[BASIC 요금제 질문]")
    basic_qs = get_best_research_questions(test_slide, rfp_requirements, SLIDE_TEMPLATES, plan_type="basic")
    for q in basic_qs:
        print(f"- {q}")

    print("\n[ADVANCED 요금제 질문]")
    advanced_qs = get_best_research_questions(test_slide, rfp_requirements, SLIDE_TEMPLATES, plan_type="advanced")
    for q in advanced_qs:
        print(f"- {q}")
