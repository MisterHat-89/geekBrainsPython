# 7. Создать вручную и заполнить несколькими строками текстовый файл, в
# котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю
# прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.


print("")
dicter = {}
average_profit = {}
avg_sum = 0
sum_m = 0
count_firm = 0
try:
    with open(r"dz7.txt", "r", encoding="utf-8") as my_file:
        for line in my_file:
            clean_line = line.replace("\n", "")
            lister = clean_line.split(" ")
            price = int(lister[2]) - int(lister[3])
            print(lister)
            if price > 0:
                avg_sum += price
            dicter[lister[0]] = price
            sum_m = 0
            count_firm += 1
    average_profit["average_profit"] = avg_sum/count_firm
except IOError:
    print("Error")
lister = [dicter, average_profit]
print("")
print(lister)
f_file = open(r"jsonDZ7.txt", "w", encoding="utf-8")
f_file.write(str(lister))
f_file.close()
print("")
print("Файл jsonDZ7.txt сохранён успешно")
