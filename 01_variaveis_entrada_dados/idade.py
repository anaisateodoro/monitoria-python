#####
# Python 
# Exercício 005
# Monitoria 30/07/24
#####

"""
Pergunte ao usuário o nome e a idade dele. Adicione 1 à idade dele e exiba a mensagem: [Nome], no próximo aniversário você terá [nova idade]
"""

# Solicita o nome e a idade do usuário
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

# Adiciona 1 à idade
nova_idade = idade + 1

# Exibe a mensagem
print(f"{nome}, no próximo aniversário você terá {nova_idade} anos.")
