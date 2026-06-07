import json

class QuestionDB:
    def __init__(self, filename):
        with open(filename, 'r', encoding="utf-8") as f:
            self.questions = json.load(f)

    def get_question(self, question_id):
        for q in self.questions:
            if q["id"]==question_id:
                return Question_v2(q)
        return None