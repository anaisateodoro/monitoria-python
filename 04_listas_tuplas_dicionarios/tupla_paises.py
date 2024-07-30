#####
# Python 
# Exercício 015
# Monitoria 30/07/24
#####

tupla_paises = ("Argentina", "Brasil", "Chile", "Equador", "Paraguai", "Venezuela")
print(tupla_paises)
print(' ')

pais = input("Por favor, digite um dos países acima: ")
print(pais, 'tem o número de índice', tupla_paises.index(pais))
