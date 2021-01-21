# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий
# название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def clean_words(string):
    return "".join(filter(str.isdigit, string))


print("")
dicter = {}
sum_m = 0
try:
    with open(r"dz6.txt", "r", encoding="utf-8") as my_file:
        for line in my_file:
            clean_line = line.replace("\n", "")
            lister = clean_line.split(" ")
            if lister[1] != "—" and lister[1] != "-":
                sum_m += int(clean_words(lister[1]))
            if lister[2] != "—" and lister[2] != "-":
                sum_m += int(clean_words(lister[2]))
            if lister[3] != "—" and lister[3] != "-":
                sum_m += int(clean_words(lister[3]))
            dicter[lister[0][:-1]] = sum_m
            sum_m = 0
except IOError:
    print("Error")

print(dicter)
