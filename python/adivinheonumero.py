import time
import random

escolha = ''

while escolha != '2':
    nome = input("Qual seu nome? ")
    print(f"Olá, {nome}. Deseja jogar o jogo de adivinhe o número? DIGITE 1 PARA JOGAR, DIGITE 2 PARA ENCERRAR! ")
    escolha = input("Qual você escolhe? ")

    if escolha == '1':

        print("Ok, vamos começar.")
        print("Irei escolher um número, aguarde...")
        time.sleep(0.5)
        x = random.randint(1, 1000)
        print("Meu número secreto foi escolhido. ")
        time.sleep(0.3)

        palpite = int(input("Escolha um número de 1 até 1000: "))

        while palpite != x:
            if palpite < x:
                print(f"Número errado. Esse numéro é MAIOR que {palpite}")
            else:
                print(f"Número errado. Esse número é MENOR que {palpite}")
            palpite = int(input("Tente novamente: "))

        print("VOCÊ ACERTOU, TAPORRA! ")

        if palpite > 1000 or palpite < 1:
            print("Esse número é inválido! ")
    elif escolha == '2':
        print("Ok, até logo...")
    else:
        print("Opção inválida!")        
