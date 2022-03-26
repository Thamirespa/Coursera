n = int(input('Digite um número inteiro:'))

soma = 0
 
while (n > 0):
    
   soma += (n //1 % 10)
   n = int(n //10)
   
print(soma) 
