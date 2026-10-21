import time

while True:
    """Pede um número inteiro até o usuário digitar um valor válido."""
    try:
        numero = int(input("Digite um número para ver a tabuada: "))
        break
    except ValueError:
        print("Digite apenas NÚMEROS inteiros! ")

print(f"\nTabuada do {numero}:")
"""Imprime a tabuada de 1 a 10 do número informado."""
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2d} = {resultado}")
    time.sleep(0.3)