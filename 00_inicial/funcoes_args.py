#####
# Python 
# Exercício 002
# Monitoria 30/07/24
#####

# *args: Usamos *args quando não sabemos ao certo quantos argumentos serão passados para uma função.
# Esses argumentos são armazenados como uma tupla.

# **kwargs: Com **kwargs, além dos valores, podemos passar as respectivas chaves para cada argumento,
# permitindo identificar cada valor pelo seu nome. Esses argumentos são armazenados como um dicionário.

def verifica_aluna(*args):
    if 'Aluna' in args and 'WoMaKerscode' in args:
        return 'Bem-vinda Aluna!'
    return 'Eu não sei quem você é aluna...'

print(verifica_aluna())
print(verifica_aluna(1, True, 'WoMaKerscode', 'Aluna'))

"""
# Exemplo de uso de **kwargs
def verifica_informacao(**kwargs):
    if kwargs.get('nome') == 'Anaísa' and kwargs.get('curso') == 'FuturoDev':
        return 'Informações corretas!'
    return 'Informações incorretas.'

    
print(verifica_informacao(nome='Anaísa', curso='FuturoDev'))
print(verifica_informacao(nome='Anaísa', curso='OutroCurso'))
"""