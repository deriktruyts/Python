# Desafio 003 - Aula 06
# Criar um programa que some dois números e exiba na tela.
# ------------------------------------------------------------------------
num1 = int(input('\033[33m • \033[mInsira um número: '))
num2 = int(input('\033[33m • \033[mInsira outro número: '))
soma = (num1 + num2)
print('\033[33m • \033[mA soma entre os números {}{}{} e {}{}{} é igual à: {}{}{}'.format('\033[36m', num1, '\033[m', '\033[36m', num2, '\033[m', '\033[33m', soma, '\033[m'))
