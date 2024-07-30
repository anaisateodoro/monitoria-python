#####
# Python 
# Exercício 006
# Monitoria 30/07/24
#####

'''
Pedir ao usuário apresentar a mensagem de saída
Olá [Primeiro nome] 
'''

primeiro_nome= input('Qual é o seu nome? ')

print('Olá{}'.format(primeiro_nome))


### Exemplos de composição com números decimais
print("%5f" % 5)
5.000000
print("%5.2f" % 5)
5.00
print("%10.5f" % 5)
5.00000

"""
O poder da composição realmente aparece quando precisamos combinar vários
valores em uma nova string. Imagine que Maria tem 21 anos e apenas R$ 51,34 na
carteira. Para exibir essa mensagem, podemos utilizar:
"""
"%s tem %d anos e apenas R$%5.2f no bolso" % ("Maria", 21, 51.34)
