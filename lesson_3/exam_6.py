# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


# Кстати, встроенная функция title(), можно использовать её, например my_string.title().
# Но так как проверяют ДЗ другие люди, функцию пришлось писать самому.

def int_func(strng):
    str_list = strng.split()
    for x in range(0, len(str_list)-1):
        str_list[x] = str_list[x].capitalize()
    return " ".join([str(elem) for elem in str_list])


string_lower_case = "it is appropriate to recall in this connection the words of a sermon by the English poet and "\
                      "priest of the xvii century John Donne which served as an epigraph to the famous novel by e. "\
                      "hemingway: \"no man is an iland, intire of it selfe; every man is a peece of the continent, "\
                      "a part of the maine; if a clod bee washed away by the sea, Europe is the lesse, as well as if "\
                      "a promontorie were, as well as if a mannor of thy friends or of thine owne were; any mans death "\
                      "diminishes me, because I am involved in mankinde; And therefore never send to know for whom the "\
                      "bell tolls; It tolls for thee\""
print("Оригинал: ")
print(string_lower_case)
print("Результат: ")
print(int_func(string_lower_case))



