from core.question_loader import QuestionLoader
from core.test_session import TestSessions
from ui.console_ui import ConsoleUI
from core.user import User
from core.settings_loader import SettingsLoader
from core.test_session import TestSession_0
from ui.console_ui import ConsoleUI_0
from core.testing import Testing

#сброс персональных данных
login_name = None
countAns = None
questions = QuestionLoader.load("data/questions.json")


while True:

    print(f"Добро пожаловать! Выберите пункт меню:")
    if login_name is None:
        print("""
    0 Выход   
    _____________                    
    1 Вход
    2 Регистрация
              """)
    else:
        print('''
    3 Режим тестирования
    4 Режим проверки знаний
    _______________________          
    9 Изменение настроек
    0 Выход''')

    select_code = int(input())
    match select_code:
        case 1:
            #print("Вход")

            #сброс персональных данных
            login_name = None
            countAns = None

            #Загружаем пользователя
            user_name = input("Введите ЛОГИН: ")
            user = User(user_name)
            user_session=user.LoadUser()
            if user_session is not None:
                print("Пользователь найден")
                login_name=user_name
                #Загружаем настройки
                settings = SettingsLoader.load()
                countAns = settings["questions_per_session"]
            else:
                #if (input("Вы уверены что не ошибл1ись в написании ЛОГИНа. Создать нового пользователя Y/N - ").lower()=="y"):
                print("Пользователь НЕ найден")
        case 2:
            print("Регистрация")

            #сброс персональных данных
            login_name = None
            countAns = None

            name = input("Введите логин нового пользователя - ")
            user=User(name)
            user.createUser()
            login_name=name
            
            #Загружаем настройки
            settings = SettingsLoader.load()
            countAns = settings["questions_per_session"]


        case 3:
            if login_name is None:
                break
            else:
                
                numbers_god_number=user_session["question_stats"]
                ans = Testing(numbers_god_number)

                for ask in range(countAns):
                   #генерируем случайное число из избранного списка за исключением вопросов на которые ранее были получены положительные ответы  
                   answers_number = ans.rand_ans()
                   print(answers_number)
                   #Подготавливаем и выводим  выбранный Вопрос
                   

                   #отвечаем на вопрос и проверяем ответ
                   
                   #если ответ правильный то записываем его в статистику класса

        case 4:
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

        case 11:
            #проверка по всем вопросам без статистики
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
