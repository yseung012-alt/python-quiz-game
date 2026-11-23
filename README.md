# Python 기초 퀴즈 게임

## 1. 프로젝트 소개

Python 기초 문법을 학습하고 복습할 수 있는 콘솔 기반 퀴즈 게임입니다.

사용자가 터미널에서 메뉴를 선택하여 퀴즈를 풀고, 새로운 문제를 추가하거나 전체 문제 목록과 최고 점수를 확인할 수 있습니다.

퀴즈 데이터와 최고 점수를 JSON 파일에 저장하여 프로그램을 종료한 후에도 기존 데이터를 사용할 수 있도록 구현했습니다.

## 2. 주제 선정 이유

Python을 공부하면서 배운 기본 개념을 문제로 풀어보고, 직접 퀴즈를 추가하며 학습 내용을 복습하기 위해 선정했습니다.

또한 Python의 조건문, 반복문, 클래스, 리스트, 딕셔너리, 함수, 파일 입출력 및 예외 처리를 하나의 프로그램에 적용하고자 했습니다.

프로젝트 개발 과정에서 Git을 활용하여 기능별 변경 사항을 관리하고, GitHub를 통해 원격 저장소 관리 방법도 실습했습니다.

## 3. 개발 환경

| 구분 | 사용 환경 |
|---|---|
| 운영체제 | Windows + WSL Ubuntu |
| 프로그래밍 언어 | Python 3.14.4 |
| 버전 관리 | Git 2.53.0 |
| 원격 저장소 | GitHub |
| 코드 편집기 | Visual Studio Code |
| 데이터 저장 방식 | JSON |
| 프로그램 실행 방식 | CLI(Command Line Interface) |

별도의 외부 Python 라이브러리를 설치하지 않고 Python 기본 기능과 표준 라이브러리인 json을 사용했습니다.

## 4. 프로젝트 구조

```text
python-quiz-game/
├── main.py
├── quiz.py
├── quiz_game.py
├── storage.py
├── test_play.py
├── test_quiz_game.py
├── state.json
├── .gitignore
└── README.md
```

| 파일명 | 역할 |
|---|---|
| main.py | 메인 메뉴 출력 및 사용자 입력 처리 |
| quiz.py | 개별 퀴즈의 문제와 정답을 관리하는 Quiz 클래스 |
| quiz_game.py | 퀴즈 목록, 게임 진행, 점수 및 데이터 관리 |
| storage.py | JSON 파일 저장 및 불러오기 |
| test_play.py | 퀴즈 진행 및 최고 점수 확인용 테스트 코드 |
| test_quiz_game.py | 퀴즈 추가 및 목록 확인용 테스트 코드 |
| state.json | 퀴즈와 최고 점수를 저장하는 실행 데이터 |
| .gitignore | Git 관리 대상에서 제외할 파일 설정 |
| README.md | 프로젝트 설명 및 실행 결과 정리 |

state.json은 프로그램 실행 중 데이터가 저장될 때 생성되며 Git 관리 대상에서는 제외합니다.

## 5. 프로그램 실행 방법

### 5-1. GitHub 저장소 복제

```bash
git clone https://github.com/yseung012-alt/python-quiz-game.git
```

git clone은 GitHub 원격 저장소에 있는 프로젝트 파일과 커밋 기록을 로컬 환경으로 복제하는 명령어입니다.

### 5-2. 프로젝트 폴더 이동

```bash
cd python-quiz-game
```

cd 명령어를 사용하여 프로그램 파일이 있는 디렉터리로 이동합니다.

### 5-3. 프로그램 실행

```bash
python3 main.py
```

main.py를 실행하면 퀴즈 게임의 메인 메뉴가 출력됩니다.

## 6. 프로그램 주요 기능

| 메뉴 번호 | 기능 | 설명 |
|---|---|---|
| 1 | 퀴즈 풀기 | 등록된 문제를 풀고 점수를 계산합니다. |
| 2 | 퀴즈 추가하기 | 새로운 문제와 정답을 등록합니다. |
| 3 | 퀴즈 목록 보기 | 등록된 전체 문제를 출력합니다. |
| 4 | 최고 점수 확인 | 현재까지 기록된 최고 점수를 출력합니다. |
| 5 | 종료 | 프로그램을 종료합니다. |

1~5 이외의 값을 입력하면 오류 안내 메시지를 출력하고 다시 메뉴를 선택할 수 있습니다.

## 7. 기본 퀴즈 구성

프로그램에 저장된 퀴즈가 없는 경우 기본 문제 5개를 등록합니다.

| 번호 | 문제 | 정답 |
|---|---|---|
| 1 | Python에서 출력할 때 사용하는 함수는? | print |
| 2 | Python에서 조건문을 만들 때 사용하는 키워드는? | if |
| 3 | Python에서 반복문에 사용하는 키워드 중 하나는? | for |
| 4 | Python에서 리스트에 항목을 추가하는 메서드는? | append |
| 5 | Python에서 함수 정의에 사용하는 키워드는? | def |

## 8. 프로그램 구현 및 코드 설명

### 8-1. Quiz 클래스 구현

파일: quiz.py

```python
class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
```

Quiz 클래스는 하나의 퀴즈에 해당하는 문제와 정답을 관리합니다.

- class: 관련 데이터와 기능을 하나의 구조로 관리합니다.
- __init__: 객체가 생성될 때 실행되는 초기화 메서드입니다.
- self.question: 퀴즈의 문제를 저장합니다.
- self.answer: 퀴즈의 정답을 저장합니다.

문제와 정답을 각각 관리하는 대신 하나의 객체로 묶어 관리하도록 구현했습니다.

### 8-2. QuizGame 클래스 초기화

파일: quiz_game.py

```python
class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0

        data = load_data()

        if data is not None and isinstance(data, dict):
            self.best_score = data.get("best_score", 0)

            for item in data.get("quizzes", []):
                self.add_quiz(item["question"], item["answer"])
```

QuizGame 클래스는 전체 퀴즈 목록과 게임 진행에 필요한 기능을 관리합니다.

- self.quizzes: 여러 개의 Quiz 객체를 저장하는 리스트입니다.
- self.best_score: 최고 점수를 저장하는 변수입니다.
- load_data(): 기존 JSON 파일의 데이터를 불러옵니다.
- isinstance(data, dict): 불러온 데이터가 딕셔너리인지 확인합니다.
- get(): 지정된 키가 없을 경우 기본값을 사용할 수 있습니다.

프로그램 실행 시 기존 데이터를 불러오며, 등록된 퀴즈가 없는 경우 기본 퀴즈 5개를 생성합니다.

### 8-3. 기본 퀴즈 생성

```python
if not self.quizzes:
    self.add_quiz("Python에서 출력할 때 사용하는 함수는?", "print")
    self.add_quiz("Python에서 조건문을 만들 때 사용하는 키워드는?", "if")
    self.add_quiz("Python에서 반복문에 사용하는 키워드 중 하나는?", "for")
    self.add_quiz("Python에서 리스트에 항목을 추가하는 메서드는?", "append")
    self.add_quiz("Python에서 함수 정의에 사용하는 키워드는?", "def")
```

if not self.quizzes는 퀴즈 리스트가 비어 있는지 확인합니다.

저장된 데이터가 없거나 JSON 파일을 정상적으로 불러오지 못한 경우에도 기본 문제를 이용하여 게임을 실행할 수 있도록 구현했습니다.

### 8-4. 퀴즈 추가 기능

```python
def add_quiz(self, question, answer):
    quiz = Quiz(question, answer)
    self.quizzes.append(quiz)
```

사용자가 입력한 문제와 정답으로 Quiz 객체를 생성합니다.

append() 메서드를 사용하여 생성한 객체를 기존 퀴즈 리스트의 마지막에 추가합니다.

### 8-5. 메인 메뉴 및 반복문

파일: main.py

```python
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
```

from과 import를 사용하여 quiz_game.py의 QuizGame 클래스를 불러옵니다.

while True는 조건이 항상 참인 반복문으로, 사용자가 프로그램을 종료할 때까지 메뉴를 반복하여 출력합니다.

input()을 통해 사용자로부터 메뉴 번호를 입력받습니다.

입력된 값에 따라 if, elif, else 조건문을 사용하여 해당 기능을 실행합니다.

### 8-6. 퀴즈 진행 및 정답 판별

파일: quiz_game.py

```python
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

    self.save_game()
```

퀴즈를 시작할 때 현재 게임 점수를 0으로 초기화합니다.

for 반복문으로 등록된 퀴즈를 순서대로 출력하며 사용자의 정답을 입력받습니다.

- strip(): 입력값 앞뒤의 공백을 제거합니다.
- lower(): 문자열을 소문자로 변환합니다.
- ==: 사용자 입력값과 정답이 같은지 비교합니다.
- score += 1: 정답을 맞힌 경우 점수를 1점 증가시킵니다.

오답인 경우 실제 정답을 함께 출력하여 사용자가 학습할 수 있도록 구현했습니다.

모든 문제를 풀면 최종 점수를 출력하고 최고 점수 갱신 여부를 확인합니다.

### 8-7. 새로운 문제 입력 및 빈 입력 처리

파일: main.py

```python
elif choice == "2":
    question = input("새로운 문제를 입력하세요: ").strip()
    answer = input("정답을 입력하세요: ").strip()

    if question and answer:
        game.add_quiz(question, answer)
        game.save_game()
        print("퀴즈가 추가되었습니다!")
    else:
        print("문제와 정답은 비워둘 수 없습니다.")
```

사용자로부터 새로운 문제와 정답을 입력받습니다.

strip()을 사용하여 불필요한 앞뒤 공백을 제거합니다.

if question and answer 조건문을 사용하여 문제와 정답이 모두 입력되었는지 확인합니다.

빈 문자열이나 공백만 입력한 경우 퀴즈를 추가하지 않고 오류 메시지를 출력합니다.

정상적으로 입력한 경우 퀴즈 리스트에 추가하고 JSON 파일에 저장합니다.

### 8-8. 퀴즈 목록 출력

```python
elif choice == "3":
    if not game.quizzes:
        print("등록된 퀴즈가 없습니다.")
    else:
        for number, quiz in enumerate(game.quizzes, start=1):
            print(f"{number}. {quiz.question}")
```

enumerate()를 사용하여 문제와 번호를 함께 가져옵니다.

start=1을 지정하여 문제 번호가 1번부터 시작하도록 구현했습니다.

퀴즈 목록이 비어 있는 경우에는 등록된 퀴즈가 없다는 안내 메시지를 출력하도록 조건문을 추가했습니다.

### 8-9. 최고 점수 관리

```python
if score > self.best_score:
    self.best_score = score
    print("새로운 최고 점수입니다!")
```

현재 게임에서 획득한 점수가 기존 최고 점수보다 높은 경우에만 최고 점수를 갱신합니다.

기존 최고 점수보다 낮은 점수를 획득하더라도 최고 점수는 유지됩니다.

```python
def show_best_score(self):
    print("현재 최고 점수:", self.best_score)
```

메뉴 4번을 선택하면 저장된 최고 점수를 확인할 수 있습니다.

### 8-10. 프로그램 종료 및 잘못된 입력 처리

파일: main.py

```python
elif choice == "5":
    print("게임을 종료합니다!")
    break

else:
    print("잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")
```

break는 실행 중인 반복문을 종료하는 명령어입니다.

5번 메뉴를 선택하면 while 반복문을 종료합니다.

등록되지 않은 메뉴 번호를 입력하면 오류 메시지를 출력하고 메인 메뉴로 돌아갑니다.

## 9. JSON 데이터 저장 및 불러오기

### 9-1. JSON 사용 목적

프로그램의 변수와 리스트는 프로그램이 종료되면 메모리에서 사라집니다.

따라서 사용자가 추가한 문제와 최고 점수를 프로그램 종료 이후에도 유지하기 위해 JSON 파일을 사용했습니다.

JSON은 데이터를 키와 값의 형태로 저장할 수 있는 파일 형식입니다.

Python의 딕셔너리와 리스트를 이용하여 데이터를 구조적으로 저장할 수 있습니다.

### 9-2. Quiz 객체를 딕셔너리로 변환

파일: quiz_game.py

```python
def save_game(self):
    quiz_data = []

    for quiz in self.quizzes:
        quiz_data.append({
            "question": quiz.question,
            "answer": quiz.answer
        })

    save_data(quiz_data, self.best_score)
```

Quiz 객체를 JSON에 저장할 수 있도록 문제와 정답을 딕셔너리 형태로 변환합니다.

변환된 데이터를 리스트에 추가하고 최고 점수와 함께 save_data() 함수로 전달합니다.

### 9-3. JSON 파일 저장

파일: storage.py

```python
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
```

- import json: Python의 JSON 처리 표준 라이브러리를 불러옵니다.
- open(): 파일을 열거나 생성합니다.
- w: 파일을 쓰기 모드로 엽니다.
- encoding="utf-8": 한글을 올바르게 저장하도록 문자 인코딩을 설정합니다.
- with: 파일 사용이 끝나면 자동으로 파일을 닫습니다.
- json.dump(): Python 데이터를 JSON 파일에 기록합니다.
- ensure_ascii=False: 한글을 읽을 수 있는 형태로 저장합니다.
- indent=4: 들여쓰기 4칸을 적용하여 파일을 읽기 쉽게 구성합니다.
- except OSError: 파일 저장 중 발생하는 운영체제 관련 오류를 처리합니다.

### 9-4. JSON 데이터 구조

state.json은 다음과 같은 구조를 사용합니다.

아래 코드는 저장 형식을 설명하기 위한 예시입니다.

```json
{
    "quizzes": [
        {
            "question": "Python에서 출력할 때 사용하는 함수는?",
            "answer": "print"
        }
    ],
    "best_score": 3
}
```

quizzes에는 문제와 정답이 저장되고, best_score에는 최고 점수가 저장됩니다.

실제 파일에는 현재 등록된 전체 퀴즈가 저장됩니다.

### 9-5. JSON 파일 불러오기 및 예외 처리

```python
def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return None
```

- r: 파일을 읽기 모드로 엽니다.
- json.load(): JSON 파일의 내용을 Python 데이터로 변환합니다.
- return data: 불러온 데이터를 반환합니다.
- FileNotFoundError: 파일이 존재하지 않는 경우 처리합니다.
- JSONDecodeError: JSON 문법이 잘못된 경우 처리합니다.
- OSError: 파일 접근 등 운영체제 관련 오류를 처리합니다.

예외가 발생하면 None을 반환합니다.

QuizGame 클래스는 불러온 데이터가 없는 경우 기본 문제 5개와 최고 점수 0점을 사용합니다.

## 10. 테스트 코드

### 10-1. 퀴즈 추가 테스트

파일: test_quiz_game.py

```python
from quiz_game import QuizGame

game = QuizGame()

game.add_quiz("출력 함수는?", "print")
game.add_quiz("반복문 키워드는?", "for")

print("퀴즈 개수:", len(game.quizzes))

for quiz in game.quizzes:
    print(quiz.question, "/", quiz.answer)
```

QuizGame 객체를 생성한 후 두 개의 퀴즈를 추가합니다.

len()을 이용하여 전체 퀴즈 개수를 확인하고 반복문으로 문제와 정답을 출력하는 테스트 코드입니다.

### 10-2. 퀴즈 진행 및 최고 점수 테스트

파일: test_play.py

```python
from quiz_game import QuizGame

game = QuizGame()

game.play_quiz()
game.show_best_score()

game.play_quiz()
game.show_best_score()
```

퀴즈를 두 번 실행하고 각각의 실행 이후 최고 점수를 확인하는 테스트 코드입니다.

두 테스트 파일은 자동화된 단위 테스트가 아니라 직접 실행하여 결과를 확인하기 위한 테스트용 스크립트입니다.

## 11. 실제 실행 결과 및 기능 검증

GitHub에 업로드한 프로젝트를 별도의 python-quiz-game-clone 디렉터리에 복제하여 주요 기능을 직접 검증했습니다.

### 11-1. 퀴즈 게임 실행 및 점수 확인

기본 문제 5개에 다음과 같이 정답을 입력했습니다.

| 번호 | 입력값 | 실제 판별 결과 |
|---|---|---|
| 1 | print | 정답 |
| 2 | if | 정답 |
| 3 | where | 오답 |
| 4 | plus | 오답 |
| 5 | def | 정답 |

실제 실행 결과 3문제를 맞혀 최종 점수 3점이 출력되었습니다.

기존 최고 점수보다 높은 점수를 획득하여 새로운 최고 점수 안내 메시지가 출력되었으며 데이터 저장 완료 메시지도 확인했습니다.

<!-- 퀴즈 실행 및 최종 점수 스크린샷 첨부 -->

### 11-2. 최고 점수 유지 확인

게임을 다시 실행하여 모든 문제에 오답을 입력했습니다.

최종 점수는 0점으로 출력되었으며 새로운 최고 점수 안내 메시지는 출력되지 않았습니다.

이후 메뉴 4번을 선택한 결과 최고 점수는 기존의 3점으로 유지되었습니다.

현재 점수가 기존 최고 점수보다 낮은 경우 최고 점수가 변경되지 않는 것을 확인했습니다.

<!-- 최고 점수 유지 스크린샷 첨부 -->

### 11-3. 새로운 퀴즈 추가

메뉴 2번을 선택하여 다음 문제를 추가했습니다.

- 문제: Python에서 길이를 구하는 함수는?
- 정답: len

문제를 입력할 때 앞부분에 공백을 포함하여 입력했습니다.

실행 결과 데이터 저장 완료 및 퀴즈 추가 완료 메시지가 출력되었습니다.

메뉴 3번으로 퀴즈 목록을 확인한 결과 기존 5개에서 6개로 증가하였으며, 추가된 문제의 앞부분 공백이 제거된 것을 확인했습니다.

<!-- 퀴즈 추가 및 전체 목록 스크린샷 첨부 -->

### 11-4. 프로그램 재실행 및 데이터 유지

프로그램을 종료한 후 다시 실행했습니다.

메뉴 3번과 4번을 선택하여 퀴즈 목록 및 최고 점수를 확인했습니다.

실제 실행 결과는 다음과 같습니다.

| 확인 항목 | 종료 전 | 재실행 후 |
|---|---|---|
| 등록된 퀴즈 개수 | 6개 | 6개 |
| 최고 점수 | 3점 | 3점 |
| 추가한 퀴즈 | 존재 | 존재 |

프로그램 종료 이후에도 JSON 파일에 저장된 데이터가 유지되는 것을 확인했습니다.

<!-- 프로그램 재실행 및 데이터 유지 스크린샷 첨부 -->

### 11-5. 잘못된 메뉴 입력

메뉴 번호에 9를 입력했습니다.

실제 실행 결과 다음 오류 메시지가 출력되었습니다.

`잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.`

프로그램이 종료되지 않고 메인 메뉴가 다시 출력되는 것을 확인했습니다.

<!-- 잘못된 메뉴 입력 스크린샷 첨부 -->

### 11-6. JSON 파일 손상 테스트

복제한 테스트용 프로젝트에서 다음 명령어를 실행하여 state.json 파일에 잘못된 데이터를 입력했습니다.

```bash
echo 'invaild json' > state.json
python3 main.py
```

JSON 형식이 아닌 데이터를 기록하여 파일을 정상적으로 불러올 수 없는 상황을 만들었습니다.

실제 실행 결과 프로그램이 오류로 종료되지 않고 정상적으로 실행되었습니다.

메뉴 3번을 선택했을 때 기본 퀴즈 5개가 출력되었으며, 메뉴 4번을 선택했을 때 최고 점수가 0점으로 초기화되었습니다.

이를 통해 잘못된 JSON 문법으로 인해 데이터를 불러올 수 없는 상황에서 기본 데이터를 사용하는 것을 확인했습니다.

해당 테스트는 원본 프로젝트에 영향을 주지 않도록 복제된 테스트용 디렉터리에서 진행했습니다.

<!-- JSON 손상 및 기본 데이터 초기화 스크린샷 첨부 -->

### 11-7. 빈 문제 및 정답 입력 테스트

메뉴 2번을 선택한 이후 문제와 정답을 입력하지 않고 Enter 키를 눌렀습니다.

실제 실행 결과 다음 메시지가 출력되었습니다.

`문제와 정답은 비워둘 수 없습니다.`

빈 데이터가 퀴즈로 등록되지 않고 메인 메뉴로 돌아가는 것을 확인했습니다.

<!-- 빈 입력 처리 스크린샷 첨부 -->

### 11-8. 전체 기능 테스트 결과

| 테스트 항목 | 실제 실행 결과 | 검증 결과 |
|---|---|---|
| 프로그램 실행 | 메인 메뉴 정상 출력 | 성공 |
| 기본 퀴즈 | 기본 문제 5개 출력 | 성공 |
| 정답 판별 | 정답 3개 처리 | 성공 |
| 오답 판별 | 오답 안내 및 실제 정답 출력 | 성공 |
| 점수 계산 | 최종 점수 3점 출력 | 성공 |
| 최고 점수 갱신 | 최고 점수 3점 저장 | 성공 |
| 최고 점수 유지 | 0점 획득 후 최고 점수 3점 유지 | 성공 |
| 퀴즈 추가 | 5개에서 6개로 증가 | 성공 |
| 퀴즈 목록 조회 | 등록된 문제 6개 출력 | 성공 |
| JSON 데이터 저장 | 저장 완료 메시지 출력 | 성공 |
| 데이터 영속성 | 재실행 후 퀴즈 6개 및 최고 점수 3점 유지 | 성공 |
| 잘못된 메뉴 입력 | 오류 안내 후 메뉴 재출력 | 성공 |
| JSON 문법 손상 | 기본 퀴즈 5개 및 최고 점수 0점 사용 | 성공 |
| 빈 문제 및 정답 입력 | 오류 메시지 출력 | 성공 |
| 프로그램 종료 | 종료 메시지 및 터미널 복귀 | 성공 |

## 12. Git 버전 관리

### 12-1. Git 저장소 초기화

```bash
git init
git branch -M main
```

git init을 사용하여 프로젝트 디렉터리를 Git 저장소로 초기화했습니다.

기본 브랜치 이름은 main으로 설정했습니다.

### 12-2. 기능별 커밋

프로그램을 한 번에 작성한 것이 아니라 기능별로 구현하고 변경 사항을 커밋했습니다.

```bash
git add .
git commit -m "커밋 메시지"
```

git add는 변경된 파일을 스테이징 영역에 등록하며, git commit은 등록된 변경 사항을 기록합니다.

### 12-3. 실제 커밋 기록

README 최종 작성 전 확인한 기존 11개의 커밋 기록입니다.

| 순서 | 커밋 ID | 커밋 메시지 |
|---|---|---|
| 1 | 0998615 | docs: initalize project documentation |
| 2 | 6ab7974 | feat: implement interactive game menu |
| 3 | c5f77eb | feat: add Quiz class |
| 4 | d80726d | feat implement quiz management |
| 5 | be19242 | feat: add five default quizzes |
| 6 | 84835c5 | feat:implement quiz play and scoring |
| 7 | e222271 | feat: track best quiz score |
| 8 | 31fe858 | feat: add JSON save and load functions |
| 9 | 2976302 | feat: integrate JSON persistence with quiz game |
| 10 | e641e01 | feat: connect quiz game menu |
| 11 | 0cf2a2a | feat: handle empty quiz list |

이후 실행 데이터 제외 설정과 README 보완 작업도 별도로 관리합니다.

### 12-4. 커밋 기록 확인

```bash
git log --oneline
```

커밋 ID와 커밋 메시지를 한 줄씩 출력하여 개발 과정과 변경 이력을 확인할 수 있습니다.

<!-- Git 커밋 기록 스크린샷 첨부 -->

### 12-5. 브랜치 생성 및 기능 구현

```bash
git switch -c feature/quiz-validation
```

기존 main 브랜치에 직접 변경 사항을 적용하지 않고 새로운 기능 개발용 브랜치를 생성했습니다.

feature/quiz-validation 브랜치에서 퀴즈 목록이 비어 있는 경우를 처리하는 조건문을 추가했습니다.

```bash
git add main.py
git commit -m "feat: handle empty quiz list"
```

해당 기능을 구현한 후 별도의 커밋으로 기록했습니다.

### 12-6. 브랜치 병합

```bash
git switch main
git merge feature/quiz-validation
```

기능 개발을 완료한 후 main 브랜치로 이동하여 변경 사항을 병합했습니다.

실제 병합 결과 Fast-forward 방식으로 병합되었으며 충돌 없이 완료되었습니다.

Fast-forward는 main 브랜치에서 별도의 변경 사항이 발생하지 않은 경우 브랜치의 위치를 새로운 커밋으로 이동시키는 병합 방식입니다.

### 12-7. 브랜치 및 작업 상태 확인

```bash
git branch -a
git status
```

git branch -a를 통해 로컬 및 원격 추적 브랜치를 확인할 수 있습니다.

git status는 현재 브랜치와 파일의 변경 상태를 확인하는 명령어입니다.

브랜치 병합 완료 후 작업 디렉터리가 변경 사항이 없는 상태임을 확인했습니다.

## 13. GitHub 원격 저장소 관리

### 13-1. 원격 저장소 연결

```bash
git remote add origin https://github.com/yseung012-alt/python-quiz-game.git
git remote -v
```

origin이라는 이름으로 GitHub 원격 저장소를 등록했습니다.

git remote -v를 통해 fetch와 push에 사용되는 원격 저장소 주소를 확인했습니다.

### 13-2. GitHub 업로드

```bash
git push -u origin main
```

로컬 main 브랜치의 커밋과 파일을 GitHub 원격 저장소에 업로드했습니다.

-u 옵션을 사용하여 로컬 main 브랜치가 원격 origin/main 브랜치를 추적하도록 설정했습니다.

실제 최초 push 결과 새로운 main 브랜치가 GitHub에 생성되었으며, 원격 브랜치 추적 설정이 완료되었습니다.

<!-- Git push 성공 스크린샷 첨부 -->

### 13-3. 원격 저장소 동기화

```bash
git pull origin main
```

원격 저장소의 변경 사항을 가져와 현재 로컬 브랜치에 통합하는 명령어입니다.

push 이후 pull 명령어를 실행하여 원격 저장소와 로컬 저장소의 동기화 과정을 실습했습니다.

### 13-4. 별도 디렉터리에 프로젝트 복제

```bash
cd ~
git clone https://github.com/yseung012-alt/python-quiz-game.git python-quiz-game-clone
```

기존 프로젝트와 별도로 복제본을 생성했습니다.

GitHub에 업로드한 파일만으로 프로그램을 정상적으로 실행할 수 있는지 검증하기 위해 진행했습니다.

복제한 프로젝트에서 퀴즈 실행, 문제 추가, 최고 점수 유지, 데이터 저장 및 예외 처리 기능을 직접 테스트했습니다.

이를 통해 원격 저장소에 업로드된 프로젝트가 다른 디렉터리에서도 정상적으로 실행되는 것을 확인했습니다.

<!-- Git clone 및 복제 프로젝트 실행 스크린샷 첨부 -->

## 14. .gitignore 설정

```gitignore
# Python 캐시 파일
__pycache__/
*.pyc

# 가상환경
.venv/
venv/

# 환경변수 및 비밀정보
.env

# 운영체제 임시 파일
.DS_Store
Thumbs.db

# 게임 실행 데이터
state.json
```

.gitignore는 Git에서 추적하지 않을 파일과 디렉터리를 지정하는 파일입니다.

Python 실행 과정에서 자동으로 생성되는 캐시 파일, 가상환경, 환경변수 파일, 운영체제 임시 파일을 제외했습니다.

state.json은 사용자별로 달라지는 실행 데이터이므로 Git 관리 대상에서 제외했습니다.

## 15. 프로젝트 구현 과정에서 발생한 문제 및 해결 방법

### 15-1. 들여쓰기 오류

Python은 들여쓰기를 기준으로 코드의 실행 범위를 구분합니다.

퀴즈 목록 검증 조건문을 추가하는 과정에서 들여쓰기 오류가 발생했습니다.

if, elif, else 조건문과 for 반복문의 들여쓰기 위치를 수정하여 해결했습니다.

### 15-2. 프로그램 종료 후 데이터 유지 문제

변수와 리스트에만 데이터를 저장하면 프로그램 종료 이후 데이터가 사라집니다.

이를 해결하기 위해 JSON 파일 저장 및 불러오기 기능을 구현했습니다.

프로그램을 재실행하여 추가된 퀴즈와 최고 점수가 유지되는 것을 확인했습니다.

### 15-3. JSON 파일 손상 문제

JSON 파일의 내용이 잘못된 경우 데이터를 정상적으로 불러오지 못할 수 있습니다.

try-except를 사용하여 JSONDecodeError를 처리하고 기본 데이터로 프로그램을 실행하도록 구현했습니다.

실제 손상된 JSON 파일을 이용한 테스트에서도 프로그램이 정상적으로 실행되었습니다.

### 15-4. JSON 테스트용 백업 명령어 오류

복제 프로젝트에서 JSON 손상 테스트를 진행하기 전 백업 파일을 생성하는 과정에서 파일명 입력 오류가 발생했습니다.

백업이 생성되지 않은 상태에서 테스트 데이터를 덮어썼기 때문에 복제본의 기존 테스트 데이터는 복원하지 못했습니다.

다만 원본 프로젝트와 GitHub 저장소의 소스 코드에는 영향을 주지 않았습니다.

이를 통해 파일을 수정하거나 삭제하기 전에 백업 명령의 성공 여부를 확인해야 한다는 점을 학습했습니다.

## 16. 한계점 및 향후 개선 사항

- JSON 문법 오류는 직접 검증했으나 파일 접근 권한 오류 등 모든 운영체제 관련 예외 상황을 테스트하지는 못했습니다.
- JSON 내부 데이터의 자료형과 필수 항목에 대한 세부 검증 기능을 추가할 수 있습니다.
- 현재 테스트 코드는 직접 결과를 확인하는 방식이며, 향후 자동화된 단위 테스트를 추가할 수 있습니다.
- 퀴즈 수정 및 삭제 기능을 추가할 수 있습니다.
- 문제 순서를 무작위로 변경하는 기능을 추가할 수 있습니다.
- 전체 문제 수와 정답률을 함께 표시하도록 개선할 수 있습니다.

## 17. 프로젝트를 통해 학습한 내용

이번 프로젝트를 통해 Python의 변수, 조건문, 반복문, 함수, 리스트, 딕셔너리 및 클래스가 실제 프로그램에서 어떻게 사용되는지 학습했습니다.

하나의 Python 파일에 모든 기능을 작성하는 대신 역할에 따라 파일을 분리하여 프로그램을 구성하는 방법을 익혔습니다.

JSON을 활용한 데이터 저장 및 불러오기 기능을 구현하면서 프로그램 종료 이후에도 데이터를 유지하는 방법을 학습했습니다.

또한 예외 처리를 통해 잘못된 입력과 파일 오류가 발생하는 상황에 대응하는 방법을 실습했습니다.

Git을 활용하여 기능별로 커밋을 생성하고 브랜치를 분리하여 작업한 후 병합하는 과정을 경험했습니다.

GitHub 원격 저장소에 프로젝트를 업로드하고 별도의 디렉터리로 복제하여 실행 결과를 검증함으로써 로컬 저장소와 원격 저장소의 관계를 이해할 수 있었습니다.