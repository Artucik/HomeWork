# *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.
# как я понял, это значит не создавать обработанный список
words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(words)):
    if words[i].isdigit() == True:
        words[i] = '"{:02}"'.format(int(words[i]))
    elif words[i].isdigit() == False and words[i].isalpha() == False:
        words[i] = '"+{:02}"'.format(int(words[i]))
words = ' '.join(words)
print(words)