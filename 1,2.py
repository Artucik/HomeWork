# задание 1, 2
def generator(x):
    for i in range(1, x + 1):
        yield i


nums = generator(15)
print(type(nums))
while True:
    try:
        print(next(nums))
    except StopIteration:
        print('Конец')
        break


print('')
gener = (i for i in range(1,15+1))
print(type(gener))
while True:
    try:
        print(next(gener))
    except StopIteration:
        break
