#Definição de um nó da árvore
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
#Inserção na árvore binária
def inserir(raiz, valor):
    if raiz is None:
        return No(valor) #Criação de vértice (nó)
    if valor < raiz.valor:
        raiz.esquerda = inserir(raiz.esquerda, valor)
    else:
        raiz.direita = inserir(raiz.direita, valor)
    return raiz

#Percurso em ordem (esquerda, raiz, direita)
def em_ordem(raiz):
    if raiz:
        em_ordem(raiz.esquerda)
        print(raiz.valor, end=' ')
        em_ordem(raiz.direita)

#Exemplo de uso
raiz = None
valores = [8, 3, 10, 1, 6, 14]
for v in valores:
    raiz = inserir(raiz, v)

print('Percurso em ordem:')
em_ordem(raiz)
