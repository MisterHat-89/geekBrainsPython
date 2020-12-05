seconds = int(input("Введите секунды > "))

if seconds < 0 < 86400:
    print("Вы либо ввели слишком большое число, либо отрицательное. Максимальное число 86400")
else:
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    print("{:02}:{:02}:{:02}".format(hours, minutes, seconds))
