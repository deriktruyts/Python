# Desafio 005 - Aula 07
# Criar um programa que exiba o ANTECESSOR e o SUCESSOR
# de um número inteiro inserido pelo usuário.
# ------------------------------------------------------------------------
print('\033[35m-=-\033[m'*12)
num = int(input('\033[33m • \033[mInsira um \033[33mnúmero\033[m inteiro: '))
print('\033[35m-=-\033[m'*12)
antec = num - 1
suces = num + 1
print('\033[36m • \033[mO \033[1;31mAntecessor\033[m de \033[33m{}\033[m é: \033[1;31m{}\033[m\n'
      '\033[36m • \033[mO \033[1;32mSucessor\033[m de \033[33m{}\033[m é \033[1;32m{}\033[m'.format(num, antec, num, suces))
print('\033[35m-=-\033[m'*12)