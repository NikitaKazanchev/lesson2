age_request= int(input("введите ваш возрост: "))

def main():
    if age_request >= 1 and age_request <= 6:
        return("учится в детском саду")
       
    elif age_request >= 7 and age_request <= 17:
        return("учится в школе")
       
    else:
        return("учится в ВУЗе или работает")
       
if __name__ == "__main__":
    a = main()
    print(a)