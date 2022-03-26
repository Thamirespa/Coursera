largura = int(input('Digite a largura:'))
altura = int(input('Digite a altura:'))


linha = 1
coluna = 1


while coluna <= altura:
    print(largura * '#', end="")
    print()
    coluna = coluna + 1 
    while coluna > 1 and coluna < altura:
        print('#' + ' ' * (largura - 2) + '#')
        coluna = coluna + 1 
