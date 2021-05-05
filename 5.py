# задание 5
import random


def get_jokes(number, repeat=True):

    """
    Эта функция генерирует случайные шутки

        Параметры:
            number(int): количество генерируемых шуток
            repeat(bool): значение по-умолчанию - True, False запрещает повторение слов в разных шутках, True разрешает

        Возращаемое значение:
            jokes(list): список сгенерированных шуток
    """

    jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    count = 0

    if repeat:  # если повторения возможны
        while count != number:
            jokes.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
            count += 1
        return jokes

    elif not repeat:  # если повторения не возможны
        while count != number:
            first = random.choice(nouns)
            second = random.choice(adverbs)
            third = random.choice(adjectives)
            if count == 0:
                joke = f'{first} {second} {third}'
                jokes.append(joke)
                count += 1

            elif count >= 1:
                jokes = ''.join(jokes)
                if first not in jokes and second not in jokes and third not in jokes:
                    jokes += f'.{first} {second} {third}'
                    count += 1
                else:
                    continue
        jokes = jokes.split('.')
        return jokes



print(get_jokes(4, False))
print(get_jokes(6))
print(get_jokes(5, False))
