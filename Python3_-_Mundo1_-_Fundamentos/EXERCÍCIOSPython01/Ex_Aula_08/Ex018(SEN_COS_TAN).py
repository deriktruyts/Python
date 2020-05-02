# Desafio 018 - Aula 08
# Criar um programa que leia um ângulo qualquer e mostre na tela o
# valor do seno, cosseno e tangente desse ângulo.
# ------------------------------------------------------------------------
import math

ca = float(input('Insira o Cateto Adjacente: '))
co = float(input('Insira o Cateto Oposto: '))

print('O valor de a² = {}² + {}² é: {:.2f}'
      .format(ca, co, math.sqrt(math.pow(ca, 2) + math.pow(co, 2))))
print('------------------------------------')
hip = math.sqrt(math.pow(ca, 2) + math.pow(co, 2))

sen = co / hip
cos = ca / hip
tg = co / ca

print('O valor do Seno é: {:.2f}\n'
      'O valor do Cosseno é: {:.2f}\n'
      'O valor da Tangente é: {:.2f}'.format(sen, cos, tg))