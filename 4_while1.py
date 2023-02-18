def hello_user():
     while True:
        user_question = input('Как дела?' )
        if user_question == "Хорошо":
            break
        
if __name__ == "__main__":
    hello_user()