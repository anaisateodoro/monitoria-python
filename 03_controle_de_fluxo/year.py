#####
# Python 
# Exercício 012
# Monitoria 30/07/24
#####

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Ano Bissexto")
else:
    print("Não é ano Bissexto")