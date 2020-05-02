# Desafio 011 - Aula 07
# Criar um programa que leia a largura e a altura de uma parede em metros,
# calcule sua área e a quantidade de tinta necessária para pintar esta parede.
# Adote que cada litro de tinta pinta uma área de 2m².
# ------------------------------------------------------------------------
larg = float(input('\033[33m • \033[mInsira a \033[31mlargura\033[m da parede (em metros): '))
alt = float(input('\033[33m • \033[mInsira a \033[31maltura\033[m da parede (em metros): '))

area = larg * alt
qtdTinta = area / 2

print('\033[30m • \033[mLargura: {}m\n'
      '\033[30m • \033[mAltura: {}m\n'
      '\033[30m • \033[mÁrea: {}m²\n'
      '\033[36m • \033[mQuantidade de tinta necessária para pintar a parede: {:.2f}L'.format(larg, alt, area, qtdTinta))