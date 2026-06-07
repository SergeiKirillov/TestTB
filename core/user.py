import json

class User:
    def __init__(self, name):
        self.name = name
    
    def LoadUser(self):
        try:
            nameUser ="data/users/"+self.name+".json" 
            with open(nameUser,"r",encoding="utf-8") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            #print("Пользователь не найден")
            return None
        except Exception as e:
            raise e
        else:
            return False
            pass


    def createUser(self):
        try:
            
            user_data = {
                "name": self.name,
                "total_tests": 0,
                "total_questions": 0,
                "total_correct": 0,
                "total_wrong": 0,
                "question_stats": {}
            }
            file_name ="data/users/"+self.name+".json" 
            with open(file_name,"w", encoding="utf-8") as file:
                json.dump(
                    user_data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )
            print(f"Пользователь {self.name} создан")
        except Exception as e:
            raise e
        
