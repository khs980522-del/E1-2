# 퀴즈 데이터 (문제, 선택지 4개, 정답 번호)
quizzes = [
    {
        "question": "태양계에서 가장 큰 행성은?",
        "choices": ["지구", "목성", "화성", "금성"],
        "answer": 2
    },
    {
        "question": "대한민국의 수도는?",
        "choices": ["부산", "인천", "서울", "대구"],
        "answer": 3
    },
    {
        "question": "물의 화학 기호는?",
        "choices": ["H2O", "CO2", "O2", "NaCl"],
        "answer": 1
    }
]

def show_menu():
    print("\n===== 🎯 상식 퀴즈 게임 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록 보기")
    print("4. 점수 확인")
    print("0. 종료")
    print("==========================")


def main():
    while True:
        show_menu()
        choice = input("메뉴를 선택하세요: ")

        if choice == "0":
            print("게임을 종료합니다. 안녕히 가세요! 👋")
            break
        else:
            print(f"[{choice}]번을 선택하셨습니다. (아직 구현 전)")


main()
