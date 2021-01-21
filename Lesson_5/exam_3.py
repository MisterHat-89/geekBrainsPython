# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
print("")
try:
    dicter = {}
    with open(r"dz3.txt", "r", encoding="utf-8-sig") as my_file:
        for line in my_file:
            splitter = line.split(" ")
            dicter[splitter[0]] = float(splitter[1].replace("\n", ""))
except IOError:
    print("Error")

print("Сотрудники, имеющие оклад менее 20 тысяч рублей: ")
print({key: elem for key, elem in dicter.items() if elem < 20000})
print("")
print("Средняя зп всех сотрудников: "+str(float('{:.2f}'.format(sum(dicter.values())/len(dicter),2)))+" руб.")

