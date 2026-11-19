from quiz import Quiz


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0

        self.add_quiz("Python에서 출력할 때 사용하는 함수는?", "print")
        self.add_quiz("Python에서 조건문을 만들 때 사용하는 키워드는?", "if")
        self.add_quiz("Python에서 반복문에 사용하는 키워드 중 하나는?", "for")
        self.add_quiz("Python에서 리스트에 항목을 추가하는 메서드는?", "append")
        self.add_quiz("Python에서 함수 정의에 사용하는 키워드는?", "def")

    def add_quiz(self, question, answer):
        quiz = Quiz(question, answer)
        self.quizzes.append(quiz)
    def play_quiz(self):
        score = 0

        for quiz in self.quizzes:
            print(quiz.question)
            user_answer = input("정답 입력: ")

            if user_answer.strip().lower() == quiz.answer.lower():
                print("정답입니다!")
                score += 1
            else:
                print("오답입니다!")
                print("정답:", quiz.answer)

        print("최종 점수:", score)

        if score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")
    def show_best_score(self):
        print("현재 최고 점수:", self.best_score)