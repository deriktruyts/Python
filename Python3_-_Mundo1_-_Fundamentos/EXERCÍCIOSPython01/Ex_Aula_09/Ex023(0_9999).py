# Desafio 023 - Aula 09
# Faça um programa qualquer que leia um número de 0 a 9999 e mostre
# na tela cada um dos dígitos separados.
# ------------------------------------------------------------------------
num = str(input('Insira um número de 0 a 9999: ')).zfill(4)
print('Número escolhido: {}'.format(num))

unidade = ('Unidade: {}'.format(num[3:4]))
dezena = ('Dezena: {}'.format(num[2:3]))
centena = ('Centena: {}'.format(num[1:2]))
milhar = ('Milhar: {}'.format(num[:1]))

print(unidade)
print(dezena)
print(centena)
print(milhar)
