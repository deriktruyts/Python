# Desafio 032 - Aula 10
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
# ------------------------------------------------------------------------
from datetime import date

ano = int(input('Insira um ano (Insira 0 para analisar o ano atual): '))
print('Ano escolhido pelo usuário:\n'
      '----------- {} -----------'.format(ano))
print('- Este ano é Bissexto?')
print('-?---?-----?-----?---?-')
if ano == 0:
    ano = date.today().year
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('- Este ano é Bissexto!')
else:
    print('- Este ano não é Bissexto.')
