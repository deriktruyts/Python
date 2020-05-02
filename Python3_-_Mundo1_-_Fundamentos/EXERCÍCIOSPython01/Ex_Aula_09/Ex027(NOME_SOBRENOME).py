# Desafio 027 - Aula 09
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# ------------------------------------------------------------------------
nome = input('Insira seu nome completo: ').strip()
print('Nome inserido pelo usuário: {}'.format(nome))

listar = nome.split()
print('Primeiro nome: {}'.format(listar[0]))
print('Sobrenome: {}'.format(listar[len(listar)-1]))