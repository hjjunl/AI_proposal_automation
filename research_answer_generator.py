# research_answer_generator.py

import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # 실제 운영 시 환경변수로 분리 권장

def summarize_research_results(question, search_results):
    """
    검색된 웹 결과를 기반으로 GPT가 요약, 검증, 출처 포함 답변을 생성한다.

    Args:
        question (str): 원본 리서치 질문
        search_results (list): SerpAPI로 수집한 [{title, snippet, url}]

    Returns:
        str: 요약된 답변 텍스트 (출처 포함)
    """
    if not search_results:
        return "신뢰할 수 있는 검색 결과가 부족하여 답변 생성이 어렵습니다."

    # 검색결과를 텍스트로 포맷팅
    sources_text = "\n".join(
        [f"[{i+1}] {item['title']}\n{item['snippet']}\n{item['url']}"
         for i, item in enumerate(search_results)]
    )

    system_prompt = """
    당신은 전문 리서치 요약가입니다.
    아래의 질문과 검색 결과들을 기반으로:
    1. 핵심 내용을 요약하고,
    2. 정확한 출처 링크를 함께 첨부해 주세요.
    3. 신뢰도 낮은 정보는 제외하고, 확실한 정보 위주로 정리해 주세요.
    출력은 3~5줄 이내로 간결하게 정리하세요.
    """

    user_prompt = f"""
    [질문]:
    {question}

    [검색 결과]:
    {sources_text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )

    answer = response['choices'][0]['message']['content']
    return answer


# --- 테스트 ---
if __name__ == "__main__":
    from search_collector import search_serpapi

    q = "2024년 양자컴퓨팅 시장 규모"
    results = search_serpapi(q)
    answer = summarize_research_results(q, results)

    print("\n[최종 요약 답변]\n")
    print(answer)
