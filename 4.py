import os

sizes = {10: 0, 100: 0, 1000: 0, '10000 and more': 0}
name = input('Название папки ')
for i in os.listdir(name):
    if os.path.isdir(name + '/' + i):
        for j in os.listdir(name + '/' + i):
            print(j, os.stat(name + '/' + i + '/' + j).st_size)
            if os.stat(name + '/' + i + '/' + j).st_size <= 10:
                sizes[10] += 1
            elif os.stat(name + '/' + i + '/' + j).st_size <= 100:
                sizes[100] += 1
            elif os.stat(name + '/' + i + '/' + j).st_size <= 1000:
                sizes[1000] += 1
            else:
                sizes['10000 and more'] += 1

print(sizes)

