# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class Zero(Exception):
    def __str__(self):
        return f"Деление на ноль запрещено"


number_one = int(input("Введите первое число: "))
number_two = int(input("Введите второе число: "))

try:
    if number_two == 0:
        raise Zero
    result = number_one / number_two
    print(result)
except Zero as text:
    print(text)


