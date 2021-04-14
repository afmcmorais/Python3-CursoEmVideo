lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche[3] = 'picole'

# inserir item
lanche.append('cookie')

# inserir item em qualquer posição
lanche.insert(0, 'hotdog')

# apagar um item pelo índice
del lanche[3]

# ou - para iliminar o último elemento pelo índice
lanche.pop()

# ou - para iliminar item pelo conteúdo
lanche.remove('pizza')

# verificar se o item existe
if 'pizza' in lanche:
    lanche.remove('pizza')

# criar lista através de range
# EM ORDEM
valores = list(range(4, 11))
# DESORDENADO
valores = [8, 2, 5, 4, 9, 3, 0]

#colocar em ordem
valores.sort()

#colocar em ordem inversa
valores.sort(reverse=True)

#saber o tamanho da lista
len(valores)


