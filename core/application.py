from core.user import User
from core.question_db import QuestionDB
from core.testing import Testing
from core.testManager import TestManager
from pathlib import Path

class Application:

    def __init__(self, ui_type="terminal", theme=None):
        self.theme=theme
        if ui_type == "rich":
            from ui.rich_ui import RichUI
            self.ui = RichUI()
        else:
            from ui.terminal_ui import TerminalUI
            self.ui = TerminalUI()
        self.current_user = None
        self.fileJSONdescript = None #Имя теста для вывода на экран
        self.selected_test=None  #имя файла выбранных тестов
        
        

    def login(self):
        self.current_user=self.ui.ask_input("Введите имя пользователя > ")
        # print(self.current_user)
        userSetting = User(self.current_user)
        count_quest = userSetting.LoadUser()
        if count_quest is None:
            self.ui.show_message("Нет такого пользователя. Зарегистрируйтесь")
            self.current_user = None
        else:
            self.ui.show_message(count_quest["questions_per_session"])
        
    def registration(self):
        try:
            self.current_user = self.ui.ask_input("Введите имя нового пользователя > ")
            newUser = User(self.current_user)
            newUser.createUser()
        except Exception as e:
            raise e
            self.ui.show_message(f"Ошибка. {e}")
               
        
    def testing(self):
        # Загружаем настройки пользователя  
        user = User(self.current_user)
        userSetting = user.LoadUser()

        #Если настроек нет то выходим  
        if userSetting is None:
            raise SystemExit
        else:
            #Загружаем вопросы
            selDB = Path("data")/ "tests" / f"{self.selected_test}.json"
            db=QuestionDB(selDB)
            
            
            number_god_session=[]
            #question_stats - ключ словаря где храниться список вопросов на которые успешно ответили
            #questions_per_session - кол-во вопросов провекрки за секцию
            #numbers_god_number - переменная в которую мы передаём список вопросов 
            #numbers_god_number=userSetting["question_stats"]
            numbers_god_number=[]
            if self.selected_test in userSetting["topics"]:
               # print(userSetting)
                numbers_god_number=userSetting["topics"][self.selected_test]["question_stats"]
            

            #try:
                #необходимо указать путь в хранилице где будут храниться пройденные вопросы 
                #numbers_god_number=userSetting["question_stats"] 
            #except KeyError as e:
                #Если нет такой секции то считаем что это первый запуск этого теста
            #    numbers_god_number=[]
            
            
            countAns =userSetting["questions_per_session"] #кол-во вопросв при тестировании
            ans = Testing(numbers_god_number) #Передаем номера вопросов  

            # Цикл вопросов от 0 до максимального кол-ва вопрсосов за секцию
            for ask in range(countAns):
                #генерируем случайное число из избранного списка за исключением вопросов на которые ранее были получены положительные ответы  
                answers_number = ans.rand_ans()

                #достаем Заданный вопрос    
                question = db.get_question(answers_number) 
                if question:
                    current_question_text = f"Вопрос {ask + 1}/{countAns}"
                    # обновляем экран с вопросом
                    self.ui.show_question(current_question_text)
                    self.ui.show_question(question.show())
                    
                    #отвечаем на вопрос и проверяем ответ                       
                    quest_number_user = int(self.ui.ask_input("\nВведите правильный ответ "))
                          
                    if question.check_answer(quest_number_user):
                        #если ответ правильный
                        self.ui.success("Правильно")
                        #если правильно то добавляем в список этот вопрос 
                        number_god_session.append(answers_number)
                    else:
                        self.ui.error("Не Правильно")
                        self.ui.show_message(f"Правильный ответ: {question.get_correct_answer()}")
                    self.ui.pause()

            #блок записи в статистику правильных ответов     
            #список номеров вопросов на которые был получен правильные ответы

            self.ui.show_message(f"Кол- во вопросов {countAns}, кол-во правильных ответов {len(number_god_session)}")
            full_ans=number_god_session
            user.save_user(self.selected_test,full_ans)


            self.ui.pause()
        



    def learning(self):
        ...

    def settings(self):
        ...

    def guest_menu(self):
        choice = self.ui.show_menu(
                    "Главное меню",
                    [
                        "Выход",
                        "Вход",
                        "Регистрация"
                    ]
                )
        match choice:
            case 1:
                self.login()
            case 2:
                self.registration()
            case 0:
                raise SystemExit
    
    def user_menu(self):
        choice = self.ui.show_menu(
                    f"Выбран пользователь: {self.current_user}",
                    [
                        "Выход",
                        "Тестирование",
                        "Проверка знаний",
                        "Настройки",
                        "Выход из учётной записи"             
                    ]
                )
        match choice:
            case 1:
                self.testing()
            case 2:
                self.learning()
            case 3:
                self.settings()
            case 4:
                self.current_user=None
            case 0:
                raise SystemExit

    def selectDB(self):
        manager = TestManager()
        tests = manager.get_tests_names()
        choice = self.ui.show_menu("Выбор тестов",tests)
        self.selected_test = tests[choice]
        self.run(self.selected_test)

    def loadDB(self,SelectTest):
        try:
            manager = TestManager()
            selectDBload = manager.load_test(SelectTest)
            self.fileJSONdescript=selectDBload["title"]
            return selectDBload
        except Exception as e:
            raise e
        
    

    def run(self, nameDb:str):
        # Проверка что файл существует
        if nameDb is not None:
            db = self.loadDB(nameDb)
            self.selected_test=nameDb # сохраняем выбранную тему в переменные класса  
        else:
            self.ui.error("База не найдена")   
            raise SystemExit

        self.ui.show_message(db["title"])
        while True:
            if self.current_user is None:
                self.guest_menu()
            else:
                self.user_menu()
    