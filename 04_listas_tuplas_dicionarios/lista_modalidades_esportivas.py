#####
# Python 
# Exercício 014
# Monitoria 30/07/24
#####

"""
Escreva uma lista de modalidades esportivas. 
Pergunte ao usuário qual é o seu preferido e adcione ao fim da lista.
Depois mostre a lista ordenada. 

"""

lista_de_modalidades = ['Vôlei','Basquete', 'Atletismo', 'Futebol']
lista_de_modalidades.append(input('Qual é a sua modalidade dos Jogos Olímpicos que mais gosta?'))
lista_de_modalidades.sort()
print(lista_de_modalidades)