import random

class TestSession:
    def __init__ (self, questions):
        
        self.correct_count=0
        self.wrong_count=0

        self.active_questions = questions.copy()

        random.shuffle(self.active_questions)
    
    def has_questions(self):
        return len(self.active_questions)>0
    
    def get_next_question(self):
        if not self.active_questions:
            return None
        
        q= self.active_questions.pop(0)
        q.shuffle_answers()
        return q
    
    def process_answer(self, question, answer_index):
        selected = question.answers[answer_index]
        
        if selected.correct:
            self.correct_count += 1
            return True
        self.wrong_count +=1
            #ошибочный вопрос возвращаем в конец очереди
        self.active_questions.append(question)

        return False 
    

