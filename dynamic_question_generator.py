# dynamic_question_generator.py

import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # 환경변수 또는 config로 관리 권장

def generate_dynamic_questions(slide_key, rfp_requirements, slide_templates):
    """
    슬라이드 목적 설명과 RFP 요구사항을 바탕으로 GPT가 맞춤형 리서치 질문을 생성하도록 함.

    Args:
        slide_key (str): 슬라이드 키 이름
        rfp_requirements (list): RFP로부터 도출된 요구사항 리스트
        slide_templates (dict): 슬라이드 키별 설명 텍스트 사전

    Returns:
        list: GPT가 생성한 리서치 질문 리스트
    """
    slide_description = slide_templates.get(slide_key, "이 슬라이드는 비즈니스 목적의 정보를 전달합니다.")

    system_prompt = """
    당신은 B2B 제안서를 작성하는 전문 리서치 컨설턴트입니다.
    각 슬라이드에 필요한 정보를 수집하기 위한 리서치 질문을 만들어야 합니다.
    주어진 슬라이드 목적과 RFP 요구사항을 바탕으로,
    슬라이드를 채우는 데 꼭 필요한 실질적이고 구체적인 질문을 2~3개 생성해 주세요.
    """

    user_prompt = f"""
    [슬라이드 키]: {slide_key}

    [슬라이드 목적 설명]:
    {slide_description}

    [RFP 요구사항 리스트]:
    {rfp_requirements}

    출력 형식:
    - 질문 1
    - 질문 2
    - 질문 3
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )

    content = response['choices'][0]['message']['content']
    questions = [line.strip("- • ") for line in content.split("\n") if line.strip()]
    return questions

# --- 테스트 예시 ---
if __name__ == "__main__":
    slide_key = "solution_overview"
    rfp_requirements = [
        "기존 딥러닝 알고리즘을 양자컴퓨팅 기반으로 전환하여 성능 개선 방안 제시",
        "실제 양자 모델을 통해 적용 가능한 예시 및 결과 도출"
    ]

    from slide_recommender import SLIDE_TEMPLATES  # 기존 템플릿 설명 사용

    result = generate_dynamic_questions(slide_key, rfp_requirements, SLIDE_TEMPLATES)
    print(f"\n[슬라이드: {slide_key}] 리서치 질문:")
    for q in result:
        print(f"- {q}")
