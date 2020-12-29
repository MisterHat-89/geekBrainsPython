string_of_user = str(input("Введите строку из нескольких строк >> "))
lister = []
if len(string_of_user) >= 3:
    lister = string_of_user.split()
    for index, item in enumerate(lister):

        print(f"{index+1} - {item[0:10]}")
else:
    print("Это не сработает!")
