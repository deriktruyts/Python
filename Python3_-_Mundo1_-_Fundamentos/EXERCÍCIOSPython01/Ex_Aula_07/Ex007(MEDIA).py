# Desafio 007 - Aula 07
# Criar um programa que leia as duas notas de um aluno, calcule, e mostre sua média.
# ------------------------------------------------------------------------
print('\033[35m-=-\033[m'*12)
nt1 = float(input('\033[33m • \033[mInsira sua primeira nota: '))
nt2 = float(input('\033[33m • \033[mInsira sua segunda nota: '))
print('\033[35m-=-\033[m'*12)

med = float(nt1+nt2)/2

print('\033[30m • \033[mSuas notas são: | {} | {} |'.format(nt1, nt2))
print('\033[35m-=-\033[m'*12)
print('\033[36m • \033[mSua média é: \033[33m{}\033[m'.format(med))
print('\033[35m-=-\033[m'*12)
print('\033[36m SITUAÇÃO: \033[m'.center(40))
if med >= 6.0:
    print('\033[1;32mAPROVADO!\033[m'.center(42))
else:
    print('\033[1;31mREPROVADO!\033[m'.center(42))
print('\033[35m-=-\033[m' * 12)