def main():

    product_sold_sum = 0
    general_sales = 0
    for one_phone in phones:
        phones_sum = sum(one_phone['items_sold'])
        phones_avg = round(phones_sum / len(one_phone['items_sold']), 2)
        print(f"Cуммарное количество продаж {one_phone['product']} {phones_sum}")
        print(f"Cреднее количество продаж {one_phone['product']} {phones_avg}")
        general_sales += phones_sum
        product_sold_sum += len(one_phone['items_sold'])

    print(f"Cуммарное количество продаж {general_sales}")
    print(f"среднее количество продаж {general_sales / product_sold_sum}")


if __name__ == "__main__":
    phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    main(phones)