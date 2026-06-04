import json
import os

from core.question import Question
from core.answer import Answer

class QuestionLoader:
    @staticmethod
    def load(filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, filename)
        with open(filename, "r",encoding="utf-8") as f:
            data = json.load(f)
        
        questions=[]

        for item in data:
3            answers = [
                Answer(a["text"], a["correct"])
                for a in item["answers"]
            ]
        questions.append(
            Question(
                item["id"],
                item["topic"],
                item["question"],
                answers,
                item.get("comment", "")
            )
        )
        return questions
