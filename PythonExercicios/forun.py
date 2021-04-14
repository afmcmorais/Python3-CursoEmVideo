# Programa que mostre na tela todos os números pares.
# No intervalo entre 1 e 50.

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p) :
    print(c)
print('Fim')
