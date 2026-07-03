
class Session:
    def __init__(self):
        self.user = None
        self.topic = None
        self.questions = []
        self.questions_index = 0
        self.correct = 0
        self.theme = None
        self.language = "ru"