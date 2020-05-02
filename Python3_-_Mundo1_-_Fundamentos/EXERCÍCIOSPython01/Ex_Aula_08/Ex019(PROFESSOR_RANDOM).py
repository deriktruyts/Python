# Desafio 019 - Aula 08
# Um professor quer sortear um dos seus quatro alunos para
# apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome do escolhido.
# ------------------------------------------------------------------------
import random

aluno1 = str(input('Insira o nome do Primeiro Aluno: '))
aluno2 = str(input('Insira o nome do Segundo Aluno: '))
aluno3 = str(input('Insira o nome do Terceiro Aluno: '))
aluno4 = str(input('Insira o nome do Quarto aluno: '))

print('O Aluno escolhido foi: {}'.format(random.choice([aluno1, aluno2, aluno3, aluno4])))