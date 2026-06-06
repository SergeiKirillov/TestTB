from core.question_loader import QuestionLoader
from core.test_session import TestSessions
from ui.console_ui import ConsoleUI
from core.user import User
from core.settings_loader import SettingsLoader

global login_name 

while True:
    print('''Добро пожаловать! Выберите пункт меню:
    1 Вход
    2 Регистрация
    3 Режим тестирования
    4 Режим проверки знаний
    9 Настройка
    0 Выход''')

    select_code = int(input())
    match select_code:
        case 1:
            #print("Вход")
            #Загружаем пользователя
            user_name = input("Введите ЛОГИН: ")
            user = User(user_name)
            if user.LoadUser():
                print("Пользователь найден")
            else:
                #if (input("Вы уверены что не ошибл1ись в написании ЛОГИНа. Создать нового пользователя Y/N - ").lower()=="y"):
                print("Пользователь НЕ найден")
        case 2:
            print("Регистрация")
            name = input("Введите логин нового пользователя - ")
            user=User(name)
            user.createUser()
        case 3:
            questions = QuestionLoader.load(
                "data/questions.json"
            )



        case 9:
            #Загружаем настройки
            settings = SettingsLoader.load()
            countAns = settings["questions_per_session"]
        case 0:
            print('Завершение работы')
            break  # Выходим из цикла
