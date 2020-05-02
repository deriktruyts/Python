# Desafio 004 - Aula 06
# Criar um programa que mostre o máximo de tipos de algo inserido pelo usuário.
# ------------------------------------------------------------------------
a = input('Digite algo: ')
print('')
print('O tipo primitivo é: ', type(a))
print('É Numérico?', a.isnumeric())
print('É Alfabético?', a.isalpha())
print('É Alfanumérico?', a.isalnum())
print('Possui apenas caracteres Minúsculos?', a.islower())
print('Possui apenas caracteres Maiúsculos?', a.isupper())
print('É Decimal?', a.isdecimal())

