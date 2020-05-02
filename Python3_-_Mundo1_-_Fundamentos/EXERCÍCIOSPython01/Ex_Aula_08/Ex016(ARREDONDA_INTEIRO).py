# Desafio 016 - Aula 08
# Criar um programa que leia um número real
# qualquer pelo teclado e mostre na tela a sua porção inteira.
# ------------------------------------------------------------------------
import math

num = float(input('Insira um número real quebrado: '))
inteira = math.floor(num)

print('A parte inteira de {} é: {}'.format(num, inteira))

