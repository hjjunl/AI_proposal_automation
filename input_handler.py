# input_handler.py

def get_user_input():
    """
    사용자로부터 RFP 작성에 필요한 입력값을 받는다.
    Returns:
        dict: RFP, 스타일, 워딩 키워드, 고객사명, 제안 제목, 고객 방향성
    """
    print("\n====== [RFP 제안서 생성 - 사용자 입력 단계] ======\n")

    # 1. RFP 원문 입력
    rfp_text = input("1. RFP 원문을 입력하세요 (길어도 괜찮습니다):\n")

    # 2. 스타일(톤) 선택
    print("\n2. 원하는 스타일(톤)을 선택하세요:")
    style_options = {
        "1": "격식 있는",
        "2": "신뢰감 있는",
        "3": "간결한",
        "4": "창의적인"
    }
    for k, v in style_options.items():
        print(f"{k}. {v}")
    style_choice = input("선택 번호 입력: ").strip()
    style_selected = style_options.get(style_choice, "신뢰감 있는")  # 기본값

    # 3. 워딩 키워드 입력
    keywords_input = input("\n3. 강조하고 싶은 워딩 키워드를 입력하세요 (쉼표로 구분):\n")
    keywords_list = [kw.strip() for kw in keywords_input.split(",") if kw.strip()]

    # 4. 고객사 명칭 (선택)
    client_name = input("\n4. 고객사 이름을 입력하세요 (없으면 Enter):\n").strip()

    # 5. 제안서 제목 (선택)
    proposal_title = input("\n5. 제안서 제목을 입력하세요 (없으면 Enter):\n").strip()

    # 6. 고객이 원하는 제안 방향성 (선택)
    user_direction = input("\n6. 고객이 원하는 제안서의 방향성을 자유롭게 서술해 주세요 (예: 실용 중심, 기술 강조 X 등):\n").strip()

    # 결과 정리
    user_inputs = {
        "rfp_text": rfp_text,
        "style": style_selected,
        "keywords": keywords_list,
        "client_name": client_name,
        "proposal_title": proposal_title,
        "user_direction": user_direction
    }

    return user_inputs

# --- 테스트 ---
if __name__ == "__main__":
    result = get_user_input()
    print("\n====== [입력 결과 요약] ======")
    for key, value in result.items():
        print(f"{key}: {value}")
