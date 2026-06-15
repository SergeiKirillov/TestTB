from abc import ABC, abstractmethod
class BaseUI(ABC):
    @abstractmethod
    def show_message(self, text):
        pass
    
    @abstractmethod
    def show_menu(self, title, options):
        pass

    @abstractmethod
    def ask_input(self, text):
        pass

    @abstractmethod
    def show_question(self, question):
        pass
