# Desafio 017 - Aula 08
# Criar um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo, calcule e mostre
# o comprimento da hipotenusa.
# ------------------------------------------------------------------------
import math

ca = float(input('Insira o Cateto Adjacente: '))
co = float(input('Insira o Cateto Oposto: '))

print('O valor de a² = {}² + {}² é: {:.2f}'
      .format(ca, co, math.sqrt(math.pow(ca, 2) + math.pow(co, 2))))