# Desafio 026 - Aula 09
# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "a".
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.
# ------------------------------------------------------------------------
frase = input('Insira uma frase: ')
print('Você inseriu a frase: {}'.format(frase))

print('Quantidade de letras "a" na frase: {}'.format(frase.count('a')))

print('A primeira letra "a" aparece na posição: {}'.format(frase.find('a'[0:])+1))
print('A última letra "a" aparece na posição: {}'.format(frase.rfind('a')+1))