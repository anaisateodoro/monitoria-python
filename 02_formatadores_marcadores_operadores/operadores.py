#####
# Python 
# Exercício 010
# Monitoria 30/07/24
#####

x = input('Digite um número: ')
print(x)

nome = input ('Digite seu nome: ')
print('Você digitou %s'%nome)
print('Olá,%s!'%nome)


"""
Escreva um algoritmo que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
String: TTAAC
Resultado:
T: 2x
A: 2x
C: 1x
"""
sequencia = input("Digite a string: ")

contador = {}

for letra in sequencia:
    contador[letra] = contador.get(letra, 0) + 1

for chave, valor in contador.items():
    print(f"{chave}: {valor}x")