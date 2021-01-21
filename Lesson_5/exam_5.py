# 5. Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

print("")
lister = "5 10 0 15 25 33 22 16 0 22"
new_file = open("dz5.txt", "w", encoding="utf-8")
new_file.write(lister)
new_file.close()
result = 0
try:
    with open(r"dz5.txt", "r", encoding="utf-8") as my_file:
        result = sum(list(map(int, my_file.read().replace("\n", "").split())))
except IOError:
    print("Error")

print("Сумма чисел = "+str(result))

