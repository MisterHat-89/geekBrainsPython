lister = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
dict_month = {"1": "Зима", "2": "Зима", "3": "Весна", "4": "Весна", "5": "Весна", "6": "Лето", "7": "Лето", "8": "Лето",
              "9": "Осень", "10": "Осень", "11": "Осень", "12": "Зима"}
number_month = int(input("Введите номер месяца от 1 до 12 >> "))
if 1 <= number_month <= 12:
    print('Это время года из листа - ' + str(lister[number_month - 1]))
    print('Это время года из словаря - ' + str(dict_month.get(f"{number_month}")))
else:
    print("Это не сработает!")
