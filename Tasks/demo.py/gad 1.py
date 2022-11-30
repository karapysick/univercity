import random

b1 = 0
b2 = 0

for i in range(10001):
    a = [0 ,1 ,0]
    a.pop(random.choice(a))
    if a[0] + a [1] == 1:
        b1 += 1
    else:
        b2 += 1


print(' Вероятность победы при смене выбора ', b1/100)
print('Вероятность победы при настаивании на своём выборе', b2/100)
