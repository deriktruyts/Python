# Desafio 035 - Aula 10
# Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo.
# ------------------------------------------------------------------------
r1 = float(input('Insira o comprimento da primeira reta: '))
r2 = float(input('Insira o comprimento da segunda reta: '))
r3 = float(input('Insira o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('As retas r1({}), r2({}) e r3({}) formam um triângulo!'.format(r1, r2, r3))
else:
    print('As retas informadas pelo usuário não formam um triângulo!')