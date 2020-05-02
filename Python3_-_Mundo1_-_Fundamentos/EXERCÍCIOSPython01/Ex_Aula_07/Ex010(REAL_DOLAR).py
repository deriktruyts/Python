# Desafio 010 - Aula 07
# Criar um programa que leia quantos reais a pessoa tem na carteira, e mostre na tela quantos
# dólares esta pessoa pode comprar.
# ------------------------------------------------------------------------
reais = float(input('\033[33m • \033[mInsira quantos reais você possui: R$'))

dolar = reais/3.27

print('\033[36m • \033[mVocê pode comprar até: $\033[32m{:.2f}\033[m!'.format(dolar))