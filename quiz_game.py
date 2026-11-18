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
        