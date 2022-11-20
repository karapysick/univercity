a = int(input('введите время'))
b = a // 60
c = a % 60
if c < 10:
     print(f' время- {b}:0{c}')
else:
     print (f' время- {b}:{c}')