# Desafio 024 - Aula 09
# Crie um programa que leia o nome de uma cidade e diga se
# ela começa ou não com o nome "Santo".
# ------------------------------------------------------------------------
nomeCidade = input('Insira o nome de uma cidade: ')
print('Você inseriu a cidade: {}'.format(nomeCidade))

print('A primeira palavra inserida nesta cidade é "Santo"?', 'Santo' in nomeCidade[:6])