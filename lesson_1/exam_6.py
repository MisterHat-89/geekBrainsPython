first_day = float(input("Введите результат за первый день > "))
need_result = float(input("Введите конечный результат > "))
count = 1

while first_day < need_result:
    first_day = float('{:.2f}'.format(first_day))
    print("{}-й день: {}".format(count, first_day))
    first_day += first_day * 0.10
    count += 1
else:
    first_day = float("{:.2f}".format(first_day))
    print("{}-й день: {}".format(count, first_day))

print("Ответ: на {}-й день спортсмен достиг результата - не менее {} км".format(count, need_result))
