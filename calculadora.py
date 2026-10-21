def soma(a, b):
    resultado = a + b
    return resultado


def subtracao(a, b):
    resultado = a - b
    return resultado


def divisao(a, b):
    resultado = a / b
    return resultado


def multiplicacao(a, b):
    resultado = a * b
    return resultado


while True:

    resposta = input("Deseja abrir a calculadora? S/N ")

    if resposta.upper() == 'S':
        while True:
            try:
                num1 = float(input("Digite o primeiro número: "))
                break
            except ValueError:
                print("Digite apenas NÚMEROS! ")

        operacao = input("Deseja fazer qual operação? (+, -, /, *) ")

        # Confere a operação logo de início, antes de pedir o segundo número
        while operacao not in ("+", "-", "/", "*"):
            print("Esse comando não está disponível!")
            operacao = input("Deseja fazer qual operação? (+, -, /, *) ")

        while True:
            try:
                num2 = float(input("Escolha o segundo número: "))
                if operacao == '/' and num2 == 0:
                    print("Não é possível dividir por 0!")
                else:
                    break
            except ValueError:
                print("Digite apenas NÚMEROS! ")

        if operacao == "+":
            resultado = soma(num1, num2)

        elif operacao == "-":
            resultado = subtracao(num1, num2)

        elif operacao == "/":
            resultado = divisao(num1, num2)

        elif operacao == "*":
            resultado = multiplicacao(num1, num2)

        print(f"{num1:g} {operacao} {num2:g} = {resultado:g}")

    elif resposta.upper() == 'N':
        print("Ok...")
        break

    else:
        print("Isso não é a resposta esperada!")