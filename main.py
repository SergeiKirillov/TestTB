from core.question_loader import QuestionLoader
from core.test_session import TestSessions
from ui.console_ui import ConsoleUI
from core.user import User
from core.settings_loader import SettingsLoader

settings = SettingsLoader.load()

user_name = input("Введите имя: ")
user = User(user_name)

questions = QuestionLoader.load(
    "data/questions.json"
)







print()
print("Тест завершён")
