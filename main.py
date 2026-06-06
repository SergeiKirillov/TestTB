from core.question_loader import QuestionLoader
from core.test_session import TestSessions
from ui.console_ui import ConsoleUI
from core.user import User
from core.settings_loader import SettingsLoader

#Загружаем настройки
settings = SettingsLoader.load()
countAns = settings["questions_per_session"]

#Загружаем пользователя
user_name = input("Введите имя: ")
user = User(user_name)
if user.LoadUser():
    print("Пользователь найден")
else:
    print("Пользователь не найден")

questions = QuestionLoader.load(
    "data/questions.json"
)







print()
print("Тест завершён")
