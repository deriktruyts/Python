# Desafio 030 - Aula 10
# Crie um programa que leia um número inteiro e mostre na tela se ele é
# PAR ou Ímpar.
# ------------------------------------------------------------------------
num = int(input('Insira um número para ver se ele é PAR ou ÍMPAR: '))
print('Você inseriu o número: {}'.format(num))

if num % 2 == 0:  # Se tiver resto da divisão por 2, é ímpar. Se não tiver resto da divisão, é par!
    print('Este número é par!')
else:
    print('Este número é ímpar!')