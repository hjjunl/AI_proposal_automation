# search_collector.py

import os
import requests

# SerpAPI 키 설정 (환경변수 사용 권장)
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY", "YOUR_SERPAPI_API_KEY")


def search_serpapi(query, num_results=8):
    """
    SerpAPI를 통해 검색어에 대한 상위 검색 결과를 수집한다.

    Args:
        query (str): 검색할 질문 문장
        num_results (int): 가져올 결과 개수 (기본 8개)

    Returns:
        list of dict: [{"title": ..., "snippet": ..., "url": ...}, ...]
    """
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": num_results
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        organic_results = data.get("organic_results", [])

        results = []
        for item in organic_results[:num_results]:
            title = item.get("title")
            snippet = item.get("snippet", "")
            link = item.get("link")
            if title and link:
                results.append({
                    "title": title,
                    "snippet": snippet,
                    "url": link
                })

        if not results:
            print(f"[경고] '{query}'에 대한 검색 결과가 부족합니다.")

        return results

    except Exception as e:
        print(f"[에러] SerpAPI 검색 실패: {e}")
        return []


# --- 테스트 ---
if __name__ == "__main__":
    test_query = "2024년 양자컴퓨팅 시장 규모"
    search_results = search_serpapi(test_query)

    print(f"\n[검색 결과 - {test_query}]")
    for idx, result in enumerate(search_results, 1):
        print(f"{idx}. {result['title']}\n{result['snippet']}\n{result['url']}\n")
