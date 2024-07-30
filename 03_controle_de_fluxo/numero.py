#####
# Python 
# Exercício 011
# Monitoria 30/07/24
#####

num1 = int (input('Digite um número: '))
total = num1
denovo = 's'
while denovo == 's':
    num2 = int(input('Digite outro número: '))
    total = total + num2
    denovo = input('Você quer adicionar outro número? (s/n)')
print('O total é ', total)
