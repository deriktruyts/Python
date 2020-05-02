# Desafio 034 - Aula 10
# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
# ------------------------------------------------------------------------
salario = float(input('Insira seu salário para calcular seu aumento: '))
print('----------------------------------------------------------------')
print('AUMENTO DE 15% PARA SALÁRIOS IGUAIS OU INFERIORES À R$1250,00!')
print('AUMENTO DE 10% PARA SALÁRIOS SUPERIORES À R$1250,00!')
print('----------------------------------------------------------------')
print('Salário anterior: R${:.2f}'.format(salario))

if salario <= 1250:
    print('Seu reajuste (+ 15%): R${:.2f}'.format(salario * 1.15))
else:
    print('Seu reajuste (+ 10%): R${:.2f}'.format(salario * 1.10))