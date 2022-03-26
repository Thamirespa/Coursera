import math

a = float(input('Digite o valor da constante a:'))
b = float(input('Digite o valor da constante b:'))
c = float(input('Digute o valor da constante c:'))

delta = float((b**2) - 4*a*c)

if delta == 0:
    y1 = (-b + math.sqrt(delta)) / (2*a)
    print('a raíz desta equação é',y1)

elif delta < 0:
    print('esta equação não possui raízes reais')
    
else:
        y1 = (-b + math.sqrt(delta))/(2*a)
        y2 = (-b - math.sqrt(delta))/(2*a)
        raizes = [y1, y2]
        raizes.sort()
        print('as raízes da equação são', raizes)
        
        
    
