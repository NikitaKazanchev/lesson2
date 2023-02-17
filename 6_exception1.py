def hello_user():
    try:
        while True:
            a = input('Как дела? ')
            if a == "Хорошо":
                break
    except KeyboardInterrupt:
        print("Пока")
            
if __name__ == "__main__":
    hello_user()