# задание 5
import time

# 1 способ
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = []
start = time.perf_counter()
for i in src:
    if i not in new:
        new.append(i)
print(time.perf_counter() - start, 'время работы')
print(new, '\n')

# 2 способ
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = time.perf_counter()
temp = list(set(src))
print(time.perf_counter() - start, 'время работы')
print(new)
