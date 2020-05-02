# Desafio 008 - Aula 07
# Criar um programa que leia um valor em metros e o exiba convertido em cm e mm.
# ------------------------------------------------------------------------
print('\033[35m-=-\033[m'*18)
m = float(input('\033[33m • \033[mInsira um valor em metro(m): '))
print('\033[35m-=-\033[m'*18)

cm = float(m*100)
mm = float(m*1000)

print('\033[30m • \033[mValor em \033[1;30mmetro(m)\033[m inserido pelo usuário: {}'.format(m))
print('\033[35m-=-\033[m'*18)
print('\033[36m • \033[mEm \033[1;34mcentímetros(cm)\033[m: {}'.format(cm))
print('\033[36m • \033[mEm \033[1;35mmilímetros(mm)\033[m: {}'.format(mm))
print('\033[35m-=-\033[m'*18)