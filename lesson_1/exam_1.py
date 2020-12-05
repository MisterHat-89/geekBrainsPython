variable_one = 15
variable_two = 17

print("Текущие числа ", variable_one, variable_two)

variable_one = int(input("Введите новое первое число > "))
variable_two = int(input("Введите новое второе число > "))
variable_string = input("Введите Ваше имя > ")

print("Пользователь {} ввёл новые числа {} и {} ".format(variable_string, variable_one, variable_two))
