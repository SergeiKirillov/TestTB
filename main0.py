from core.question_loader import QuestionLoader
from core.test_session import TestSession_0
from ui.console_ui import ConsoleUI_0


questions = QuestionLoader.load(
    "data/questions.json"
)

session = TestSession_0(questions)
ui = ConsoleUI_0()

while session.has_questions():

    q = session.get_next_question()

    answer = ui.ask_question(q)

    if session.process_answer(q, answer):
        print("Верно")
    else:
        print("Неверно")

print()
print("Тест завершён")
print(f"Правильных: {session.correct_count}")
print(f"Ошибок: {session.wrong_count}")