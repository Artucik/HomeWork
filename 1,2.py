# задание 1, задание 2
def num_translate(word):
    translate = {
        'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
        'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десть'
    }
    return translate.get(word.lower())


print(num_translate('One'))
print(num_translate('seven'))
print(num_translate('qwe'))
