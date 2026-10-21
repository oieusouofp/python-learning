notas = [8.5, 4.2, 9.5, 6.0, 3.0, 7.0, 10.0, 5.5]
aprovados = []
reprovados = []
recuperacao = []

for nota in notas:
    if nota >= 7.0:
        print(f"Nota {nota}: Você Passou!")
        aprovados.append(nota)
    elif nota < 5.0:
        print(f"Nota {nota}: Você Reprovou!")
        reprovados.append(nota)
    else:
        print(f"Nota {nota}: Você está de Recuperação!")
        recuperacao.append(nota)

print("Notas Aprovadas:", aprovados)
print("Notas Reprovadas:", reprovados)
print("Notas em Recuperação:", recuperacao)