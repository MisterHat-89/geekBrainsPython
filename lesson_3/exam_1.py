# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Деление на ноль можно, но запрещено"


a = int(input("Введите число a >> "))
b = int(input("Введите число b >> "))

print("Результат >> " + str(division(a, b)))
