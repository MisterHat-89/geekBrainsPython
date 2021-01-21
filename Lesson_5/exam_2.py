# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

text = ""
f_file = open(r'dz2.txt', 'r')

print(f_file.read())
print("")
count_words = 0
lines = 0
f_file.seek(0)
for line in f_file.readlines():
    lines += 1
    count_words = len(line.split(" "))
    print(f"В строке {lines} - {count_words} слов")

f_file.close()


print(f"Строк {lines}")
