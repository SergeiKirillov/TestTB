from core.user import User
from core.question_db import QuestionDB
from core.testing import Testing


class Application:

    def __init__(self, ui):
        self.ui = ui
        self.current_user = None
        

    def login(self):
        self.current_user=self.ui.ask_input("Введите имя пользователя > ")
        print(self.current_user)
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
        user = User(self.current_user)
        userSetting = user.LoadUser()

        if userSetting is None:
            raise SystemExit
        else:
            #Загружаем вопросы
            db=QuestionDB("data/questions.json")
                
            numbers_god_number=[]
            number_god_session=[]
            numbers_god_number=userSetting["question_stats"]
            countAns =userSetting["questions_per_session"]
            ans = Testing(numbers_god_number) #Передаем номера вопросов  

            # Цикл вопросов от 0 до максимального кол-ва вопрсосов за секцию
            for ask in range(countAns):
                #генерируем случайное число из избранного списка за исключением вопросов на которые ранее были получены положительные ответы  
                answers_number = ans.rand_ans()
                    
                question = db.get_question(answers_number) #достаем Заданный вопрос
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
            user.save_user(full_ans)
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

    def run(self):
        while True:
            if self.current_user is None:
                self.guest_menu()
            else:
                self.user_menu()
