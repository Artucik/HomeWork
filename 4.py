# задание 4
lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(lst)):
    lst[i] = lst[i].split()
print(lst)

for i in lst:
    print(f'Привет, {i[-1].capitalize()}!')
