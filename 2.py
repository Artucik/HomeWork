# задание 2
# старался делать по алгоритму на сайте, а так решил бы по-другому
words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(words)):
    if words[i].isdigit() == True:
        words[i] = '" {:02} "'.format(int(words[i]))
    elif words[i].isalpha() == False and words[i].isdigit() == False:
        words[i] = '" +{:02} "'.format(int(words[i]))

words = ' '.join(words)
words = words.split()  # создал обработанный список, как в примере на сайте

for i in range(len(words)):
    if words[i].isalpha() == True:
        words[i] = f' {words[i]} '

words = ''.join(words)
print(words)