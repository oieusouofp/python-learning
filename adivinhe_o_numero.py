import time
import random

nome = input("Qual seu nome? ")
escolha = ''

while escolha != '2':
    print(f"Olá, {nome}. Deseja jogar o jogo de adivinhe o número? DIGITE 1 PARA JOGAR, DIGITE 2 PARA ENCERRAR! ")
    escolha = input("Qual você escolhe? ")

    if escolha == '1':

        print("Ok, vamos começar.")
        print("Irei escolher um número, aguarde...")
        time.sleep(0.5)
        x = random.randint(1, 1000)
        print("Meu número secreto foi escolhido. ")
        time.sleep(0.3)

        tentativas = 0
        acertou = False
        mensagem = "Escolha um número de 1 até 1000: "

        while not acertou:
            try:
                palpite = int(input(mensagem))
            except ValueError:
                print("Digite apenas NÚMEROS! ")
                continue

            if palpite > 1000 or palpite < 1:
                print("Esse número é inválido! ")
                continue

            tentativas += 1

            if palpite < x:
                print(f"Número errado. Esse número é MAIOR que {palpite}")
            elif palpite > x:
                print(f"Número errado. Esse número é MENOR que {palpite}")
            else:
                acertou = True
            mensagem = "Tente novamente: "

        print(f"VOCÊ ACERTOU em {tentativas} tentativa(s)!")
    elif escolha == '2':
        print("Ok, até logo...")
    else:
        print("Opção inválida!")