# задание 4, решено не совсем как надо
def thesaurus_adv(*args):
    surnames_word = {}
    names_word = {}
    for i in args:
        surname_letter = i[i.index(' ')+1]
        surnames_word[surname_letter] = {}
    for letter in surnames_word.keys():

        for name in args:
            names_word[name[0]] = [j for j in args if j[0] == name[0] and j[j.index(' ')+1] == letter]

        surnames_word[letter].update(names_word)

    # for i in surnames_word.values():  # каждый словарь словаря
    #     for j in i.keys():  # каждый ключ в словаре словарей
    #         if i[j] == []:
    #             i.pop(j)

    return dict(sorted(surnames_word.items()))


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева" ))
