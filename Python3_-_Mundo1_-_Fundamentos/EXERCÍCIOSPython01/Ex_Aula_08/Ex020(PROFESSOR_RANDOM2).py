# Desafio 020 - Aula 08
# O mesmo professor do desafio anterior (Ex019) quer sortear a
# ordem de apresentação de trabalhos dos alunos. Faça um
# programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# ------------------------------------------------------------------------
import random

aluno1 = str(input('Insira o nome do Primeiro Aluno: '))
aluno2 = str(input('Insira o nome do Segundo Aluno: '))
aluno3 = str(input('Insira o nome do Terceiro Aluno: '))
aluno4 = str(input('Insira o nome do Quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

sequencia = random.sample(lista, 4)

print('A ordem é: {}'.format(sequencia))