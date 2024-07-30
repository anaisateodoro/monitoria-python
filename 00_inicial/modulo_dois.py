#####
# Python 
# Exercício 003
# Monitoria 30/07/24
#####

from datetime import datetime

# Dados sobre a primeira medalha olímpica brasileira
ano_primeira_medalha = 1996
categoria_medalha = "vôlei de praia"
tipo_medalha = "ouro"


ano_atual = datetime.now().year

# Mensagem sobre a medalha olímpica
mensagem_olimpica = (
    f"Nos Jogos {ano_primeira_medalha}, a dupla fez história como as primeiras medalhistas olímpicas de {tipo_medalha} do Brasil. "
    f"Vinte anos depois, elas relembram os bastidores daquela conquista no {categoria_medalha}."
)

print(mensagem_olimpica)

# Cálculo dos anos desde a conquista
anos_passados = ano_atual - ano_primeira_medalha
print(f"Já se passaram {anos_passados} anos desde aquela conquista!!!")