lister = []
count_elements = int(input("Введите количество элементов в списке >> "))

for i in range(0, count_elements):
    elem = int(input(f"Введите {i + 1}-й элемент >> "))
    lister.append(elem)

print("list before " + str(lister))
for i in range(0, len(lister) - 1, 2):
    if i + 1 <= len(lister) - 1:
        lister[i], lister[i + 1] = lister[i + 1], lister[i]
print("list after " + str(lister))
