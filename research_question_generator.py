# research_question_generator.py

SLIDE_RESEARCH_QUESTION_TEMPLATES = {
    "market_analysis_market_overview": [
        "현재 이 시장의 규모와 성장률은?",
        "향후 5년간 시장 트렌드는 어떻게 변화할 것으로 예상되는가?"
    ],
    "growth_trend_analysis": [
        "최근 기술 성장률의 연도별 추세는?",
        "향후 기술 확산에 영향을 줄 핵심 요소는 무엇인가?"
    ],
    "competitive_benchmarking": [
        "주요 경쟁사의 기술 전략 또는 사업 전략은 어떻게 다른가?",
        "경쟁사 대비 우리 기술의 차별점은 무엇인가?"
    ],
    "solution_overview": [
        "우리가 제안하는 핵심 솔루션은 어떤 문제를 해결하는가?",
        "기존 방식 대비 이 솔루션의 기술적/사업적 강점은?"
    ],
    "strategic_recommendations": [
        "핵심 추진 전략은 어떤 것들이 있는가?",
        "경쟁력 확보를 위한 전략 포인트는 무엇인가?"
    ],
    "implementation_plan": [
        "단계별 실행 계획에서 가장 중요한 마일스톤은 무엇인가?",
        "리소스 배분은 어떻게 이루어져야 효과적인가?"
    ],
    "risk_management_plan": [
        "기술/시장/조직 측면의 주요 리스크는 무엇이며, 대응 방안은?",
        "프로젝트 실패 가능성을 낮추는 핵심 요인은 무엇인가?"
    ],
    "expected_benefits": [
        "이 제안이 고객에게 제공하는 구체적인 기대 효과는?",
        "정량적으로 측정 가능한 효과 지표는 무엇인가?"
    ]
}

def generate_research_questions(slide_key):
    """
    슬라이드 키에 따라 적절한 리서치 질문 리스트 반환
    """
    return SLIDE_RESEARCH_QUESTION_TEMPLATES.get(slide_key, [
        "해당 슬라이드 주제와 관련된 기본적인 시장 조사 및 기술 분석이 필요합니다."
    ])

# --- 테스트 ---
if __name__ == "__main__":
    test_slide = "competitive_benchmarking"
    questions = generate_research_questions(test_slide)
    print(f"\n[{test_slide}] 슬라이드용 리서치 질문:")
    for q in questions:
        print(f"- {q}")
