dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
diasrodados = dias * 60
kmrodado = km * 0.15
total = diasrodados + kmrodado

print('O total a pagar é de R${:.2f}.'.format(total))