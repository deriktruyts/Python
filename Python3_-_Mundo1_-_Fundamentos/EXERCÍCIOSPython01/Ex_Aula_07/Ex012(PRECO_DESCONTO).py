# Desafio 012 - Aula 07
# Criar um programa que leia o preço de um produto e mostre na tela atualizado com 5% de desconto.
# ------------------------------------------------------------------------
preco = float(input('Insira o valor de seu produto: R$'))

desc = preco * 0.05
precoDesc = preco - desc

print('O valor de seu produto sem desconto: R${:.2f}\n'
      'O valor de seu produto com desconto de 5%: {:.2f}\n'
      'Você teve um desconto de: R${:.2f}'.format(preco, precoDesc, desc))