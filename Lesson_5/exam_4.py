# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

print("")
try:
    my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    lister = []
    with open(r"dz4.txt", "r", encoding="utf-8") as my_file:
        for line in my_file:
            clean_line = line.replace("\n", "")
            numbers = clean_line.split(" ")[0]
            clean_line = clean_line.replace(numbers, my_dict[numbers])
            lister.append(clean_line)

except IOError:
    print("Error")
new_file = open("dz4NEW.txt", "w", encoding="utf-8")
for line in lister:
    new_file.write(line+"\n")
new_file.close()
print("Файл dz4NEW.txt сохранён успешно")

