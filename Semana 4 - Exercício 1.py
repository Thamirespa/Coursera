n = int(input('Digite o valor de n:'))
contador = n
fatorial = 1

while contador > 0:

    fatorial *= contador
    contador -= 1

print(fatorial)
