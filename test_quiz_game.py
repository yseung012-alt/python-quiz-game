from quiz_game import QuizGame

game = QuizGame()

game.add_quiz("출력 함수는?", "print")
game.add_quiz("반복문 키워드는?", "for")

print("퀴즈 개수:", len(game.quizzes))

for quiz in game.quizzes:
    print(quiz.question, "/", quiz.answer)