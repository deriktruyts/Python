# Desafio 031 - Aula 10
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
# 200Km e R$0,45 para viagens mais longas.
# ------------------------------------------------------------------------
viagem = float(input('Insira a distância (em Km/h) da viagem na qual deseja fazer: '))
print('-=-' * 23)
print('- PARA VIAGENS COM UMA DISTÂNCIA DE ATÉ 200Km/h: R$0,50 POR KM!\n'
      '- PARA VIAGENS COM UMA DISTÂNCIA SUPERIOR A 200Km/h: R$0,45 POR KM!')
print('-=-' * 23)
print('A distância da viagem inserida pelo usuário é de: {}Km/h.'.format(viagem))
print('---' * 20)

if viagem <= 200:
    print('VALOR TOTAL DA PASSAGEM (R$0,50 POR KM): R${:.2f}'.format(viagem * 0.50))
    print('---' * 20)
else:
    print('VALOR TOTAL DA PASSAGEM (R$0,45 POR KM): R${:.2f}'.format(viagem * 0.45))
    print('---' * 20)