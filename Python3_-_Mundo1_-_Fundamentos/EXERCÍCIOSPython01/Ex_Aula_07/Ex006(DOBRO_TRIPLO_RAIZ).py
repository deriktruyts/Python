# Desafio 006 - Aula 07
# Criar um programa que leia um número e mostre seu dobro, triplo e raiz quadrada.
# ------------------------------------------------------------------------
print('\033[35m-=-\033[m'*12)
num = float(input('\033[33m • \033[mInsira um número qualquer: '))
print('\033[35m-=-\033[m'*12)

dobro = num*2
triplo = num*3
raiz = (num ** (1/2))

print('\033[30m • \033[mValor inserido pelo usuário: {}'.format(num))
print('\033[35m-=-\033[m'*12)
print('\033[36m • \033[mO \033[1;32mDobro\033[m é: {}\n'
      '\033[36m • \033[mO \033[1;33mTriplo\033[m é: {}\n'
      '\033[36m • \033[mA \033[1;34mRaiz Quadrada\033[m é: {:.2f}'
      .format(dobro, triplo, raiz))
print('\033[35m-=-\033[m'*12)