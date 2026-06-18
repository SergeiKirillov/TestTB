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

    def success(self, text):
        print(text)
    
    def error(self, text):
        print(text)

    def pause(self):
        input("\nНажмите Enter для продолжения...")

