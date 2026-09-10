import random
import time
opção = ''
while opção != '2':

    print("DIGITE 1 PARA JOGAR: ")
    time.sleep(0.2)
    print("DIGITE 2 PARA SAIR: ")
    time.sleep(0.2)
    opção = input('Deseja jogar na megasena? ')
    if opção == '1':
        meu_palpite = []
        for i in range(6):
            num = int(input(f"Digite o {i + 1}º número (1 a 60): "))
            meu_palpite.append(num)

        megasena = random.sample(range(1, 61), 6)

        acertos = []

        for numero in meu_palpite:
            if numero in megasena:
                acertos.append(numero)
        
        print(f"Os números da megasena são {megasena}")
        if len(acertos) >= 1:
            print(f"Seus acertos foram {acertos}")
        else:
            print("Você não acertou nada! Fraco!")
        if len(acertos) ==  6:
            print(f"VOCÊ TEM {len(acertos)} ACERTOS! VOCÊ GANHOU UM MILHÃO!!!!!")
        elif len(acertos) == 5:
            print(f"VOCÊ TEM {len(acertos)} ACERTOS! Você quase acertou tudo, acertou 5! Parabéns pelo prêmio de 200 mil reais!")
        elif len(acertos) == 4:
            print(f"VOCÊ TEM {len(acertos)} ACERTOS! Passou muito perto, parabéns pelos 20 mil")
        else:
            print(f"VOCÊ TEM {len(acertos)} ACERTOS! Você não conseguiu dessa vez! Deseja tentar de novo?")
    elif opção == '2':
        print('Ok! Até logo... ')
    else:
        print("Esse comando não existe!")