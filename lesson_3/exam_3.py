# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def  my_func(a, b, c):
    lister = [a, b, c]
    maximum_one = max(*lister)
    lister.remove(maximum_one)
    maximum_two = max(lister)
    return maximum_one + maximum_two


print("Результат >> " + str(my_func(5, 75, 15)))

