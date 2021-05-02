# задание 5

# A
print('A')
prices = [23.5, 3, 90, 90.5, 545, 233.9, 400.5, 59.9, 69.9, 670, 300, 100, 2, 999.99, 10.11, 20.65, 90.01, 80.02, 1]
for price in prices:
    price = str(price)
    if '.' not in price:
        price += '.00'
    price = price.split('.')
    if len(price[1]) == 2:
        print('{:02} руб {:02} коп'.format(int(price[0]), int(price[1])), end=' , ')
    elif len(price[1]) != 2:
        print('{:02} руб {}0 коп'.format(int(price[0]), int(price[1])), end=' , ')
print('\n')

# B
print('B')
for i in range(len(prices)):
    prices[i] = float(prices[i])
print(prices, id(prices))
print(sorted(prices), id(sorted(prices)))
print(prices, id(prices))
print('')

# C
print('C')
prices_new = prices.copy()
prices_new.sort(reverse=True)
print(prices_new)
print('')

# D
print('D')
prices_new = prices.copy()
prices_new.sort()
for i in prices_new[-5:]:
    print(i, end=' ')
