# Desafio 028 - Aula 10
# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# ------------------------------------------------------------------------
from random import randint
from time import sleep

r = randint(0, 5)
print('-=-' * 22)
print('[COMPUTADOR]: Irei pensar em um número de 0 a 5, tente adivinhar!')
print('-=-' * 22)
n = int(input('Insira um número de 0 a 5: '))
print('Processando...')
sleep(3)
if r == n:
    print('[COMPUTADOR]: Parabéns, você acertou o número que eu escolhi!')
else:
    print('[COMPUTADOR]: Errado! Mais sorte na próxima vez')
    print('[COMPUTADOR]: Eu escolhi: {}'.format(r))
print('[COMPUTADOR]: Foi ótimo jogar com você!')