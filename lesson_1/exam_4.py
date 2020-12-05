# Не понимаю почему все так любят while, если через for было бы правильнее в данном случае

numbers = input("Введите положительное число > ")
number_symbol = 0
max_number = 0

while True:
    if int(numbers[number_symbol]) > max_number:
        max_number = int(numbers[number_symbol])
    number_symbol += 1
    if number_symbol > len(numbers) - 1:
        break

print("Максимальное число = ", max_number)
