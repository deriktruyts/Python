# Desafio 009 - Aula 07
# Criar um programa que leia um número inteiro e mostre sua tabuada.
# ------------------------------------------------------------------------
from time import sleep

num = int(input('Insira um número inteiro: '))
print('--------------------------')

t1 = num * 1
t2 = num * 2
t3 = num * 3
t4 = num * 4
t5 = num * 5
t6 = num * 6
t7 = num * 7
t8 = num * 8
t9 = num * 9
t10= num * 10

print('\033[1:33mProcessando...\033[m')
print('--------------------------')
sleep(3)
print('   \033[1:36mTABUADA DO NÚMERO:\033[m \033[1:30m{}\033[m\n'
      '     \033[1:30m>\033[m  {} x 1 = {}\n'
      '     \033[1:30m>\033[m  {} x 2 = {}\n'
      '     \033[1:30m>\033[m  {} x 3 = {}\n'
      '     \033[1:30m>\033[m  {} x 4 = {}\n'
      '     \033[1:30m>\033[m  {} x 5 = {}\n'
      '     \033[1:30m>\033[m  {} x 6 = {}\n'
      '     \033[1:30m>\033[m  {} x 7 = {}\n'
      '     \033[1:30m>\033[m  {} x 8 = {}\n'
      '     \033[1:30m>\033[m  {} x 9 = {}\n'
      '     \033[1:30m>\033[m  {} x 10 = {}'.format(num, num, t1, num, t2, num, t3, num, t4, num, t5, num, t6, num, t7,
                                 num, t8, num, t9, num, t10))
print('--------------------------')