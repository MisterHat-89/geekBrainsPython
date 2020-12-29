all_list = []
dict_items = {"Название": [], "Цена": [], "Количество": [], "Ед.": "шт."}

index = 1
while True:
    print("Заполнение нового товара в БД")
    name_item = input("Введите название товара >> ")
    name_price = float(input("Введите цену товара >> "))
    name_count = int(input("Введите количество товара >> "))
    all_list.append((index, {"Название": name_item, "Цена": name_price, "Количество": name_count, "Ед.": "шт."}))
    index += 1
    exits = input("Для выхода напишите 'Да' >> ")
    if exits == "Да":
        break

for item in all_list:
    dict_items.get("Название").append(item[1].get("Название"))
    dict_items.get("Цена").append(item[1].get("Цена"))
    dict_items.get("Количество").append(item[1].get("Количество"))

print("Аналитика товаров в БД")

print(dict_items)
