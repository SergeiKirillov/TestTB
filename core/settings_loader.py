import json


class SettingsLoader:
    
    @staticmethod
    def load():
        with open("data/settings.json","r",encoding="utf-8") as f:
            data = json.load(f)
            
            """
            data - type - list
            data[0] - type - dict
         
            
        questions=[]

        for item in data:
            answers = [
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
         """
        return True

