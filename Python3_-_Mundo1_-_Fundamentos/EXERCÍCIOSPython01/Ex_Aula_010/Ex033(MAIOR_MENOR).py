# Desafio 033 - Aula 10
# Faça um programa que leia três números e mostre qual é o maior e qual
# é o menor.
# ------------------------------------------------------------------------
num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
num3 = int(input('Insira o terceiro número: '))

if num3 > num1 and num3 > num2:
    maior = num3
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num1

if num3 < num1 and num3 < num2:
    menor = num3
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num1

print('- O maior número: {}\n- O menor número: {}'.format(maior, menor))
