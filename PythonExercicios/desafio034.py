'''s = float(input('Qual é o salário do funcionário? R$ '))
s1 = s + s * 10 / 100
s2 = s + s * 15 / 100
if s > 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s, s1))
else:
    print('Quem ganhava RS{:.2f} passa a ganhar R${:.2f} agora'.format(s, s2))'''

salário = float(input('Qual é o salário do funcionário? R$ '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salário, novo))
