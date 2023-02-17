phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def phones_sold(total_dedicated_phones):
    sold_sum = 0
    for sold in total_dedicated_phones:
        sold_sum += sold
    return sold_sum 

product_sold_sum = 0
general_sales = 0
for one_phone in phones:
    phones_avg = phones_sold(one_phone['items_sold'])
    phones_avg2 = round(phones_avg / len(one_phone['items_sold']), 2)
    print(f"Cуммарное количество продаж {one_phone['product']} {phones_avg}")
    print(f"Cреднее количество продаж {one_phone['product']} {phones_avg2}")
    general_sales += phones_avg
    product_sold_sum += len(one_phone['items_sold'])

print(f"Cуммарное количество продаж {general_sales}")
print(f"среднее количество продаж {general_sales / product_sold_sum}")
