# задание 3
def thesaurus(*args):
    names = {}
    for i in args:
        names[i[0]] = [j for j in args if i[0] == j[0]]
    return dict(sorted(names.items()))  # отсортированный по ключам список


print(thesaurus("Иван", "Мария", "Петр", "Илья", 'Артур', 'Петя', 'Маша', "Вася", "Алена", "Виктор", "Денис", "Влад"))