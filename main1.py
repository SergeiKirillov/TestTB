from core.question_loader import QuestionLoader
from core.test_session import TestSessions
from ui.console_ui import ConsoleUI
from core.user import User
from core.settings_loader import SettingsLoader
from core.test_session import TestSession_0
from ui.console_ui import ConsoleUI_0
from core.testing import Testing
from core.question_db import QuestionDB

#from colorama import init, Fore, Back, Style
from rich import print #https://habr.com/ru/articles/962608/
from rich.progress import Progress
from rich.live import Live
from rich.console import Console
from rich.panel import Panel
console = Console()

#сброс персональных данных
login_name = None
countAns = None
questions = QuestionLoader.load("data/questions.json")

#init(autoreset=True) #Инициализация colorama для корректной работы в Windows
print(f"\nДобро пожаловать!") 
while True:

    print(f"Выберите пункт меню:")
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
                print("[bold green]Пользователь найден[/bold green]")
                login_name=user_name
                #Загружаем настройки
                #settings = SettingsLoader.load()
                #countAns = settings["questions_per_session"]
                countAns = user_session["questions_per_session"]
            else:
                #if (input("Вы уверены что не ошибл1ись в написании ЛОГИНа. Создать нового пользователя Y/N - ").lower()=="y"):
                print("[bold red]Пользователь НЕ найден[/bold red]")

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
            # settings = SettingsLoader.load()
            # countAns = settings["questions_per_session"]
            user_session=user.LoadUser()
            countAns = user_session["questions_per_session"]

        case 3:
            if login_name is None:
                break
            else:
                #Загружаем вопросы
                db=QuestionDB("data/questions.json")
                
                numbers_god_number=[]
                number_god_session=[]
                numbers_god_number=user_session["question_stats"]
                ans = Testing(numbers_god_number)

                # === PROGRESS BAR ===
                progress = Progress()
                task = progress.add_task("Тест", total=countAns)

                current_question_text = "Подготовка..."

                def render_screen():
                    return Panel(
                        progress,
                        title=f"[bold cyan]Тестирование знаний[/]",
                        subtitle=current_question_text
                    )

                with Live(render_screen(), console=console, refresh_per_second=10) as live:

                    for ask in range(countAns):
                        # обновляем описание (текущий вопрос)

                        #генерируем случайное число из избранного списка за исключением вопросов на которые ранее были получены положительные ответы  
                        answers_number = ans.rand_ans()
                        #print(answers_number)
                        #Подготавливаем и выводим  выбранный Вопрос

                        question = db.get_question(answers_number)
                        if question: 
                        
                            current_question_text = f"Вопрос {ask + 1}/{countAns}"
                            # обновляем экран с вопросом
                            live.update(render_screen())
                        
                            question.show()
                            #отвечаем на вопрос и проверяем ответ                       
                            quest_number_user = int(input("\nВведите правильный ответ "))
                          
                    
                            if question.check_answer(quest_number_user):
                                #если ответ правильный
                                #print(Back.GREEN+Fore.BLACK+"Правильно")
                                console.print("[bold green]Правильно[/bold green]")
                                #если правильно то добавляем в список этот вопрос 
                                number_god_session.append(answers_number)
                            else:
                                #print(Back.RED+Fore.WHITE+"Неправильно")
                                console.print("[bold red]Неправильно[/bold red]")
                                console.print(f"Правильный ответ: {question.get_correct_answer()}")
                        progress.update(task, advance=1)
                        

                    #блок записи в статистику правильных ответов     
                    #список номеров вопросов на которые был получен правильные ответы
                    console.print(f"Кол- во вопросов {countAns}, кол-во правильных ответов {len(number_god_session)}")
                    full_ans=number_god_session
                    user.save_user(full_ans)
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
