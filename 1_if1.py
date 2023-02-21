def main():
    age = int(input("введите ваш возрост: "))
    if 1 <= age <= 7:
        return "учится в детском саду"
       
    elif age <= 17:
        return "учится в школе"
       
    else:
        return "учится в ВУЗе или работает"
       
if __name__ == "__main__":
    user_response = main()
    print(user_response)