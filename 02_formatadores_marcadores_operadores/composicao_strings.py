#####
# Python 
# Exercício 008
# Monitoria 30/07/24
#####

"""O poder da composição realmente aparece quando precisamos combinar vários
valores em uma nova string. Imagine que Maria tem 21 anos e apenas R$ 51,34 na
carteira. Para exibir essa mensagem, podemos utilizar:"""

"%s tem %d anos e apenas R$%5.2f no bolso" % ("Maria", 21, 51.34)

nome = "Maria"
idade = 21
grana = 51.34
print("%s tem %d anos e R$%f no bolso." % (nome, idade, grana))
print("%12s tem %3d anos e R$%5.2f no bolso." % (nome, idade, grana))
print("%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, grana))
print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, grana))
