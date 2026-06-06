import json

class User:
    def __init__(self, name):
        self.name = name
    
    def LoadUser(self):
        try:
            nameUser ="data/users/"+self.name+".json" 
            with open(nameUser,"r",encoding="utf-8") as f:
                data = json.load(f)
                return True
        except FileNotFoundError:
            #print("Пользователь не найден")
            return False
        except Exception as e:
            raise e
        else:
            return False
            pass


    def createUser(self, username):
        try:
            print("создание пользователя")
        except Exception as e:
            raise e
