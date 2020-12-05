print("Значение вводятся в формате рубли.копейки, например 167.32, где 167 - это рубли, 32 - копейки")
print("-" * 10)
money = float(input("Введите выручку > "))
costs = float(input("Введите издержки > "))

if money > costs:
    print(f"Фирма отработала в прибыль равную {int(money - costs)} руб. {int(((money - costs) % 1) * 100)} коп.")
    print(f"Рентабельность составила {int((money - costs) / money * 100)}%")
    count_pers = int(input("Введите количество сотрудников фирмы > "))
    money_for_every_pers = (money - costs) / count_pers
    print(f"Прибыль на каждого сотрудника составила {int(money_for_every_pers)} руб. {int((money_for_every_pers % 1) * 100)} коп.")
else:
    print(f"Фирма отработала в убыток в размере {int(costs - money)} руб. {int(((costs - money) % 1) * 100)} коп.")
