with open('users.csv', mode='r', encoding='UTF-8') as users:
    names = users.readlines()
with open('hobby.csv', mode='r', encoding='UTF-8') as hobbys:
    hobbys = hobbys.readlines()
new_file = open('new_file.txt', 'w', encoding='UTF-8')

for i in range(len(names)):
    names[i] = names[i].replace('\n', '')
for i in range(len(hobbys)):
    hobbys[i] = hobbys[i].replace('\n', '')
print(names)

if len(hobbys) == len(names):
    pairs = str(dict(zip(names, hobbys)))
    new_file.write(pairs)
elif len(hobbys) < len(names):
    new_file.write('1')
elif len(hobbys) > len(names):
    new_file.write('None')

new_file.close()
