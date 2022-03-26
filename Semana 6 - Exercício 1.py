def partida():

    print(' ')
    
    n = int(input('Quantas peças?'))
    m = int(input('Limite de peças por jogada?'))
    
    while m < 1:
        print("A quantidade de peças por jogadas devem ser menor ou igual as peças totais")
        m = int(input("Limite de peças por jogada? "))

    valor = 0
    jogada = 0

    if (n % (m+1)) == 0:
        print("\nVocê começa!")
        jogada = 1 
        while n > 0:
            if jogada == 1:
                valor = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", valor, "peça(s).")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 2
            else:
                valor = computador_escolhe_jogada(n, m)
                print("\nO computador tirou", valor, "peça(s)")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 1
                
        if jogada == 1:
            print("Fim do jogo! O computador ganhou!\n")
            return 2 
        else:
            print("Fim do jogo! O você ganhou!\n")
            return 1 
                
    else:
        print("\nComputador começa!")
        jogada = 2 
        while n > 0:
            if jogada == 2:
                valor = computador_escolhe_jogada(n, m)
                print("\nO computador tirou", valor, "peça(s)")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 1
            else:
                valor = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", valor, "peça(s).")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 2
                
        if jogada == 1:
            print("Fim do jogo! O computador ganhou!\n")
            return 2 
        else:
            print("Fim do jogo! O você ganhou!\n")
            return 1


def usuario_escolhe_jogada(n, m):

    print('Sua vez!')

    jogada = 0

    while jogada == 0:

        jogada = int(input('Quantas peças irá tirar?'))
        if jogada > n or jogada < 1 or jogada > m:
            print("\nOops! Jogada inválida! Tente de novo.\n")

            jogada = 0
            
    return jogada

def computador_escolhe_jogada(n, m):

    print('Vez do computador')

    if n <= m:
        return n
    else:
        quantia = n % (m+1)

        if quantia > 0:
            return quantia
        return m

def campeonato():
    a = 1
    usuario = 0
    computador = 0


    while a <= 3:
       
        vencedor = partida()

        if vencedor == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1
            
    print("\n**** Final do campeonato! ****\n")
    print('Placar final: Voce {} x computador {}'.format(usuario, computador))



tipo_jogo = 0

while tipo_jogo == 0:
    print('Bem vindo ao jogo do NIM! Escolha:')
    print(' ')
    print('1 - Para jogar uma partida isolada')
    print('2 - Para jogar um campeonato')

    tipo_jogo = int(input('Sua opção:'))
    print(' ')

    if tipo_jogo == 1:
        print('Você escolheu partida isolada!')
        partida() 
        break
    
    elif tipo_jogo == 2:
        print('Voce escolheu um campeonato!')
        campeonato()
        break
    else:
        print('Opção inválida!')
        tipo_jogo = 0


    
    
    
        
            

    
    
    





