import math

a = float(input('Digite o valor da constate a:'))
b = float(input('Digite o valor da constate b:'))
c = float(input('Digite o valor da constate c:'))

delta = float(b**2 - 4*a*c)

if delta == 0:
    y1 = (-b + Math.sqrt(delta)) / (2*a)
    print(' A raíz dessa equação é:', y1)

else:
    if delta < 0:
print('Essa equação não possui raízes reais.')
    else:
        y1 = (-b + Math.sqrt(delta))/(2*a)
        y2 = (-b - Math.sqrt(delta))/(2*a)
    print('As raízes da equação são:', y1, y2)
