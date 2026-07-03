
class Session:
    def __init__(self):
        self.user = None
        self.topic = None #Название теста для элемента title
        self.questions = []
        self.questions_index = 0
        self.correct = 0
        self.theme = None #имя файла где лежат тесты
        self.ui = None
        self.language = "ru"