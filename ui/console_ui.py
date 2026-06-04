class ConsoleUI:

    def ask_question(self, question):

        print()
        print(question.question)

        for i, answer in enumerate(question.answers, start=1):
            print(f"{i}. {answer.text}")

        return int(input("Ваш ответ: ")) - 1