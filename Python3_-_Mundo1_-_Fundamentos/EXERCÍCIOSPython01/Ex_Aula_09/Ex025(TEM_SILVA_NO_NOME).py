# Desafio 025 - Aula 09
# Crie um programa que leia o nome de uma pessoa e diga se
# ela tem "Silva" no nome.
# ------------------------------------------------------------------------
nome = input('Insira um nome: ')
print('Você inseriu o nome: {}'.format(nome))

print('Este nome possui "Silva"?', 'Silva' in nome)