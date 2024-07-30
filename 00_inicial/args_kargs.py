#####
# Python 
# Exercício 001
# Monitoria 30/07/24
#####

# Mini-Bio das devs

def mini_bio(**dados_pessoais):
  for key, value in dados_pessoais.items():
        print(f"{key} - {value}")
print("###Mini-Biografia###")
mini_bio(nome="Ana Maria", especialista="Back-end", linguagem="Python", senioridade="Pleno")
mini_bio(nome="Maria Clara", especialista="Front-end", linguagem="JavaScript", senioridade="Sênior")
mini_bio(nome="Aline", especialista="Fullsctack", linguagem="Javascript", senioridade="Júnior")