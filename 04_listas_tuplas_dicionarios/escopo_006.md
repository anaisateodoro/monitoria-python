### 📚 Listas

Uma lista é uma sequência ordenada de valores, que podem ser de tipos diferentes.Uma lista é uma sequência de valores, podendo conter elementos do mesmo tipo (homogênea) ou de tipos diferentes (heterogênea).

```python
animais = ["gato", "cachorro", "pássaro", "leão"]
professora = ["Maria", 30, 1.75, True]
```

**Homogênea**: elementos do mesmo tipo (ex: _strings_).
  ```python
  animais = ["gato", "cachorro", "pássaro", "leão"]
```

**Heterogênea**: diferentes tipos de dados
  ```python
professora = ["Isadora", 26, 1.70, true]
```
Listas são ordenadas e acessamos seus elementos pelo índice, começando em 0:
```python
professora[0] # "Isadora"
professora[1] # 26
professora[2] # 1.70
professora[3] # true
```

### 📖 Dicionário
Um dicionário armazena dados em pares chave-valor, ideal para representar relações. Cada elemento é composto por uma chave e um valor associado.
 ```python
pessoa = {
  "nome": "Paula",
  "idade": 29,
  "filhas": ["Luisa", "Maria"]
}
```

### 🚫 NoneType

O `NoneType` em Python simboliza o vazio. Embora seja um conceito abstrato, podemos imaginar que todos os outros tipos são caixas que contêm coisas dentro. No caso do `NoneType`, a caixa está vazia.

#### 👉 Exemplo de código:

```python
# Inicializando uma variável com None
caixa_vazia = None

# Verificando o tipo da variável
print(type(caixa_vazia))  # <class 'NoneType'>

# Uso comum de NoneType em funções
def find_element(lista, elemento):
    for item in lista:
        if item == elemento:
            return item
    return None  # Retorna None se o elemento não for encontrado

resultado = find_element([1, 2, 3], 4)
print(resultado)  # None
