# Desafio 013 - Aula 07
# Criar um programa que leia o salário de um funcionário e mostre seu novo salário, com 15%
# de aumento.
# ------------------------------------------------------------------------
salario = float(input('Insira o salário: R$ '))

salarioAum15 = salario * 1.15
salarioAum = salarioAum15 - salario

print('Salário antigo: R${:.2f}\n'
      'Salário com aumento de 15%: R${:.2f}\n'
      'Você teve um aumento de: R${:.2f}'.format(salario, salarioAum15, salarioAum))