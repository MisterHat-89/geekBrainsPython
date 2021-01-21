# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение
# факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def my_gen(n):
    fact = 1
    for item in range(1, n + 1):
        fact *= item
        yield fact


N = int(input("Введите число N: "))
result = 0
for elem in my_gen(N):
    result = elem
strings = [' * ' + str(elem) for elem in range(2, N + 1)]
print(f"Факториал {N}! = 1{''.join([str(elem) for elem in strings])} = {result}")