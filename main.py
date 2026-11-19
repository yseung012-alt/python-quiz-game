from quiz_game import QuizGame

game = QuizGame()

while True:
    print("\n===== Python 기초 퀴즈 게임 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가하기")
    print("3. 퀴즈 목록 보기")
    print("4. 최고 점수 확인")
    print("5. 종료")
    print("==============================")

    choice = input("메뉴 번호를 선택하세요: ")

    if choice == "1":
        game.play_quiz()

    elif choice == "2":
        question = input("새로운 문제를 입력하세요: ").strip()
        answer = input("정답을 입력하세요: ").strip()

        if question and answer:
            game.add_quiz(question, answer)
            game.save_game()
            print("퀴즈가 추가되었습니다!")
        else:
            print("문제와 정답은 비워둘 수 없습니다.")

    elif choice == "3":
        for number, quiz in enumerate(game.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    elif choice == "4":
        game.show_best_score()

    elif choice == "5":
        print("게임을 종료합니다!")
        break

    else:
        print("잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")