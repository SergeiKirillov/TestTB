from ui.base_ui import BaseUI

class TerminalUI(BaseUI):
    def show_menu(self, title, options):
        print(title)
        for i, opt in enumerate(options, 0):
            print(i, opt)
        return int(input(">"))
    
    def show_message(self, text):
        print(text)

    def ask_input(self, text):
        return input(text)

    def show_question(self, question):
        print(question)

    def show_question(self, question_num, total_questions, question_id, question_text, answers):
        print(f"Вопрос {question_id}({question_num + 1}/{total_questions})")
        print(question_text)
        que_show=""
        for i, answer in enumerate(answers, start=1):
            que_show = que_show + f"{i}. {answer['text']}\n"
        print(que_show)
        #отвечаем на вопрос и проверяем ответ 
        return int(input("\nВведите правильный ответ ")) 


    def success(self, text):
        print(text)
    
    def error(self, text):
        print(text)

    def pause(self):
        input("\nНажмите Enter для продолжения...")

