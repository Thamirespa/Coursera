número = float(input('digite o número:'))

resto_3 = número % 3
resto_5 = número % 5

if resto_3 == 0 and resto_5 == 0:
    print('FizzBuzz')

else:
    print(número)
