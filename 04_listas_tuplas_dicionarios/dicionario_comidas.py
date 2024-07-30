#####
# Python 
# Exercício 013
# Monitoria 30/07/24
#####

dicionario_comida = {}

dicionario_comida[1] = input('Escreva a sua primeira comida preferida: ')
dicionario_comida[2] = input('Escreva a sua segunda comida preferida: ')
dicionario_comida[3] = input('Escreva a sua terceira comida preferida: ')
dicionario_comida[4] = input('Escreva a sua quarta comida preferida: ')

print(dicionario_comida)

try:
    naocurte = int(input('Qual comida você não curte? (Escolha o número correspondente): '))
    if naocurte in dicionario_comida:
        del dicionario_comida[naocurte]
    else:
        print(f"O número {naocurte} não corresponde a nenhuma comida na lista.")
except ValueError:
    print("Entrada inválida! Por favor, digite um número.")

print(sorted(dicionario_comida.values()))

