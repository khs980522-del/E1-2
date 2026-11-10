import json
import os

QUIZ_FILE = "quizzes.json"
SCORE_FILE = "score.json"


# ============================================
# 1️⃣ Quiz 클래스 : 퀴즈 "1개"를 표현
# ============================================
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question   # 문제 (문자열)
        self.choices = choices     # 선택지 4개 (리스트)
        self.answer = answer       # 정답 번호 (정수)

    def is_correct(self, user_input):
        """사용자 입력이 정답인지 판별"""
        return user_input == str(self.answer)

    def to_dict(self):
        """JSON 저장용 → 딕셔너리로 변환"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }


# ============================================
# 2️⃣ QuizGame 클래스 : 게임 "전체"를 관리
# ============================================
class QuizGame:
    def __init__(self):
        self.quizzes = []          # Quiz 객체들을 담는 리스트
        self.best_score = 0        # 최고 점수
        self.load_quizzes()        # 시작 시 파일에서 불러오기
        self.best_score = self.load_high_score()

    # ---------- 파일 입출력 ----------
    def load_quizzes(self):
        """파일에서 퀴즈를 불러와 Quiz 객체로 변환"""
        try:
            with open(QUIZ_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = default_quizzes   # 파일 없으면 기본 퀴즈 사용

        # 딕셔너리 → Quiz 객체로 변환해서 담기
        self.quizzes = [
            Quiz(q["question"], q["choices"], q["answer"]) for q in data
        ]

    def save_quizzes(self):
        """Quiz 객체들을 딕셔너리로 바꿔 파일에 저장"""
        data = [quiz.to_dict() for quiz in self.quizzes]
        with open(QUIZ_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_high_score(self):
        if os.path.exists(SCORE_FILE):
            with open(SCORE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return 0

    def save_high_score(self, score):
        with open(SCORE_FILE, "w", encoding="utf-8") as f:
            json.dump(score, f)

    # ---------- 메뉴 ----------
    def show_menu(self):
        print("\n===== 🎯 상식 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 점수 확인")
        print("0. 종료")
        print("==========================")

    # ---------- 퀴즈 풀기 ----------
    def play_quiz(self):
        print("\n----- 퀴즈 풀기 시작! -----")
        score = 0

        for i, quiz in enumerate(self.quizzes, 1):
            print(f"\n[문제 {i}] {quiz.question}")      # quiz['question'] → quiz.question
            for num, choice in enumerate(quiz.choices, 1):
                print(f"  {num}. {choice}")

            while True:
                answer = input("정답 번호를 입력하세요 (1~4): ")
                if answer in ["1", "2", "3", "4"]:
                    break
                print("⚠️ 1~4 사이의 숫자를 입력하세요.")

            if quiz.is_correct(answer):               # Quiz의 메서드 사용!
                print("정답입니다! ⭕")
                score += 1
            else:
                print(f"틀렸습니다! ❌ 정답은 {quiz.answer}번입니다.")

        print("\n----- 퀴즈 끝! -----")
        total = len(self.quizzes)
        print(f"🏆 최종 점수: {total}문제 중 {score}문제 정답!")

        if score > self.best_score:
            self.best_score = score
            self.save_high_score(score)
            print("🎉 새로운 최고 점수를 달성했습니다!")

    # ---------- 퀴즈 추가 ----------
    def add_quiz(self):
        print("\n----- 새 퀴즈 추가 -----")
        question = input("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}번: ")
            choices.append(choice)

        answer = int(input("정답 번호를 입력하세요 (1~4): "))

        new_quiz = Quiz(question, choices, answer)   # Quiz 객체 생성!
        self.quizzes.append(new_quiz)
        self.save_quizzes()
        print("✅ 퀴즈가 추가되었습니다!")

    # ---------- 퀴즈 목록 ----------
    def show_quizzes(self):
        print("\n===== 📋 등록된 퀴즈 목록 =====")
        if len(self.quizzes) == 0:
            print("아직 등록된 퀴즈가 없습니다.")
            return
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"{i}. {quiz.question}")

    # ---------- 점수 확인 ----------
    def show_high_score(self):
        print("\n===== 🏆 최고 점수 =====")
        print(f"지금까지 최고 점수: {self.best_score}점")

    # ---------- 메인 루프 ----------
    def run(self):
        while True:
            self.show_menu()
            choice = input("메뉴를 선택하세요: ")

            if choice == "0":
                print("게임을 종료합니다. 안녕히 가세요! 👋")
                break
            elif choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quizzes()
            elif choice == "4":
                self.show_high_score()
            else:
                print("⚠️ 잘못된 입력입니다. 0~4 사이의 숫자를 입력하세요.")


# 기본 퀴즈 데이터 (파일이 없을 때 사용)
default_quizzes = [
    {"question": "태양계에서 가장 큰 행성은?", "choices": ["지구", "목성", "화성", "금성"], "answer": 2},
    {"question": "대한민국의 수도는?", "choices": ["부산", "인천", "서울", "대구"], "answer": 3},
    {"question": "물의 화학 기호는?", "choices": ["H2O", "CO2", "O2", "NaCl"], "answer": 1},
    {"question": "1 + 1 은?", "choices": ["1", "2", "3", "4"], "answer": 2},
    {"question": "무지개는 몇 가지 색?", "choices": ["5", "6", "7", "8"], "answer": 3},
]


# ============================================
# 프로그램 실행
# ============================================
game = QuizGame()   # 게임 객체 만들고
game.run()          # 실행!