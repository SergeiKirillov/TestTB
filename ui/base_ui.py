from abc import ABC, abstractmethod
class BaseUI(ABC):
    @abstractmethod
    def show_message(self, text:str):
        pass
    
    @abstractmethod
    def show_menu(self, title, options):
        pass

    @abstractmethod
    def ask_input(self, text:str):
        pass

    @abstractmethod
    def show_question(self, question):
        pass

    @abstractmethod
    def success(self, text: str):
        pass

    @abstractmethod
    def error(self, text: str):
        pass

    @abstractmethod
    def pause(self):
        pass