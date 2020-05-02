# Desafio 022 - Aula 09
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas;
# - O nome com todas minúsculas;
# - Quantas letras ao total (sem contar os espaços);
# - Quantas letras tem o primeiro nome.
# ------------------------------------------------------------------------
nome = input('Insira seu nome completo: ')
print('Seu nome completo: {}'.format(nome))

print('Seu nome com as letras em maiúsculo: {}'.format(nome.upper()))
print('Seu nome com as letras em minúsculo: {}'.format(nome.lower()))

listar = nome.split()
print('Seu nome sem espaços possui {} caracteres'.format(len(''.join(listar))))
print('Somente seu primeiro nome possui {} caracteres'.format(len(listar[0])))

