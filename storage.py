import json

FILE_NAME = "state.json"


def save_data(quizzes, best_score):
    data = {
        "quizzes": quizzes,
        "best_score": best_score
    }

    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("데이터 저장 완료!")

    except OSError as error:
        print("데이터 저장 실패:", error)

def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return None