# slide_recommender.py

import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # 환경변수로 관리 추천

SLIDE_TEMPLATES = {
    "project_understanding": "고객이 요청한 과제의 본질을 정확히 이해하고 있음을 보여주는 슬라이드입니다.",
    "client_needs_summary": "고객사의 주요 니즈와 기대사항을 명확하게 요약 정리하는 슬라이드입니다.",
    "market_analysis_market_overview": "목표 시장의 규모, 성장률, 트렌드, 주요 산업 변화 요인을 소개하는 슬라이드입니다. 시장 진입 전략이나 성장 가능성을 보여주기 위해 사용됩니다.",
    "growth_trend_analysis": "시장 혹은 제품군의 성장 패턴을 시계열 그래프로 분석하여 설명하는 슬라이드입니다.",
    "industry_drivers_challenges": "시장 성장을 촉진하는 요인과 장애 요인을 나누어 분석하는 슬라이드입니다.",
    "competitive_benchmarking": "주요 경쟁사들의 전략, 제품, 시장 점유율 등을 정리하고 비교하는 슬라이드입니다.",
    "swot_analysis": "자사 또는 제안 솔루션의 강점(Strengths), 약점(Weaknesses), 기회(Opportunities), 위협(Threats)을 분석하는 슬라이드입니다.",
    "solution_overview": "제안하는 솔루션의 핵심 특징과 기대 효과를 요약 소개하는 슬라이드입니다.",
    "strategic_recommendations": "고객 과제를 해결하기 위한 구체적 전략 방안을 제시하는 슬라이드입니다.",
    "implementation_plan": "제안한 전략을 실행하기 위한 구체적 단계별 실행 로드맵을 정리한 슬라이드입니다.",
    "timeline_milestones": "전체 프로젝트 일정과 주요 마일스톤을 시각적으로 표시하는 슬라이드입니다.",
    "risk_management_plan": "프로젝트 수행 중 발생할 수 있는 주요 리스크와 대응 방안을 정리한 슬라이드입니다.",
    "expected_benefits": "제안 솔루션 도입 시 고객이 얻을 수 있는 기대 효과를 요약한 슬라이드입니다."
}

def recommend_slides_llm(requirements):
    """
    요구사항 리스트를 기반으로, 각 슬라이드 설명과 비교하여 GPT가 적절한 슬라이드를 추천
    Args:
        requirements (list): 요구사항 텍스트 목록
    Returns:
        list: 추천된 슬라이드 키 리스트
    """
    system_prompt = """
    당신은 제안서 자동화 시스템의 전문가입니다.
    아래에 주어진 요구사항 리스트와 슬라이드 설명을 비교하여,
    각 요구사항에 가장 부합하는 슬라이드 템플릿을 추천해 주세요.
    출력은 슬라이드 key 이름만 리스트로 반환하세요.
    """

    user_prompt = f"""
    [요구사항 리스트]:
    {requirements}

    [슬라이드 템플릿 설명]:
    {SLIDE_TEMPLATES}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )

    raw_output = response['choices'][0]['message']['content']
    slide_keys = [line.strip("- • ") for line in raw_output.strip().split("\n") if line.strip()]
    return slide_keys

# --- 테스트 ---
if __name__ == "__main__":
    test_requirements = [
        "시장 성장률을 분석하고 최신 트렌드를 반영해야 함",
        "유사 과제 및 경쟁사 분석을 포함",
        "실행 단계별 세부 계획 수립 필요",
        "예상되는 리스크와 대응 방안 포함 필요"
    ]

    results = recommend_slides_llm(test_requirements)
    print("\n[GPT 기반 추천 슬라이드 키]")
    for key in results:
        print(f"- {key}")
