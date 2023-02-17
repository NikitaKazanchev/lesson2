questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Пиво будешь?": "Конечно"}

def ask_user(answers_dict):
    while answers_dict:
        a = input("Введи вопрос ")
        if a in answers_dict:
            print(f"Пользователь: {a}")
            print(f"Программа: {answers_dict[a]}")
            break
        else:
            print("Пока")
        
    
if __name__ == "__main__":
    ask_user(questions_and_answers)