def ask_user(answers_dict):
    while answers_dict:
        user_question = input("Введи вопрос ")
        if user_question in answers_dict:
            print(f"Пользователь: {user_question}")
            print(f"Программа: {answers_dict[user_question]}")
            break
        else:
            print("Пока")
        
    
if __name__ == "__main__":
    questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Пиво будешь?": "Конечно"}
    ask_user(questions_and_answers)