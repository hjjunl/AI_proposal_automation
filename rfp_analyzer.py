# rfp_analyzer.py

import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # 보안을 위해 환경변수로 관리 권장

def analyze_rfp(rfp_text, direction_text=""):
    """
    RFP 원문과 방향성을 바탕으로 요약 및 요구사항 도출

    Args:
        rfp_text (str): 원본 RFP 텍스트
        direction_text (str): 고객의 방향성 텍스트

    Returns:
        dict: {"summary": 요약문, "requirements": 요구사항 리스트}
    """
    system_prompt = """
    당신은 전문 제안서 분석가입니다. 아래 RFP 내용을 바탕으로:
    1. 간결한 요약문을 작성하고
    2. 제안서 작성 시 고려해야 할 핵심 요구사항을 항목별로 나열하세요.
    고객이 원하는 방향성이 주어진 경우, 이를 중심에 두고 요약과 요구사항을 작성하세요.
    """

    user_prompt = f"""
    [RFP 본문]:
    {rfp_text}

    [고객 방향성]:
    {direction_text if direction_text else '없음'}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )

    result_text = response['choices'][0]['message']['content']

    # 간단한 파싱 처리 (요약문과 요구사항 구분)
    lines = result_text.strip().split("\n")
    summary = []
    requirements = []
    is_req = False
    for line in lines:
        if line.strip().startswith("-") or line.strip().startswith("\u2022"):
            is_req = True
            requirements.append(line.strip("- •"))
        elif not is_req:
            summary.append(line.strip())

    return {
        "summary": " ".join(summary),
        "requirements": requirements
    }

# --- 테스트 ---
if __name__ == "__main__":
    test_rfp = """
    본 공모는 양자컴퓨팅 기반의 머신러닝 기술 전환을 위한 과제이며,
    MLP, CNN, RNN 등 기존 딥러닝 구조의 양자 최적화가 주요 목표입니다.
    연구는 실용화를 목적으로 하며, 데모 시스템 구현까지 포함되어야 합니다.
    """
    direction = "기술 설명은 최소화하고 실용화 방향 중심으로 작성해줘."

    result = analyze_rfp(test_rfp, direction)
    print("\n[요약]\n", result['summary'])
    print("\n[요구사항]\n")
    for i, req in enumerate(result['requirements'], 1):
        print(f"{i}. {req}")
