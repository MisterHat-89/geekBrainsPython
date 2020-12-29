lister = [7, 5, 3, 3, 2]
print("Таблица рейтинга " + str(lister))

while True:
    numb_of_user = int(input("Введите следующее число "))
    lister.append(numb_of_user)
    lister.sort(reverse=True)

    print("Новая таблица рейтинга " + str(lister))
    exits = input("Для выхода напишите 'Да' >> ")
    if exits == "Да":
        break
