import math

x1 = float(input('Digite o primeiro valor:'))
y1 = float(input('Digite o segundo valor:'))
x2 = float(input('Digite o terceiro valor:'))
y2 = float(input('Digite o quarto valor:'))

d = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

if d >=10:
    print('longe')
else:
    print('perto')

