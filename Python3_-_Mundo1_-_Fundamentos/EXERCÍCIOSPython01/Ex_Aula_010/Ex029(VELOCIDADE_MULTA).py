# Desafio 029 - Aula 10
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
# ------------------------------------------------------------------------
velocidade = float(input('Insira a velocidade (em Km/h) atual de seu veículo: '))
print('-=-' * 7)
print('Velocidade: {}Km/h'.format(velocidade))
print('-=-' * 7)

if velocidade > 80:
    print('----------------------- MULTADO! -----------------------')
    print('[DETRAN]: CADA KM ACIMA DO LIMITE IRÁ LHE CUSTAR R&7,00')
    print('[DETRAN]: Valor total: R${:.2f}'.format((velocidade - 80) * 7))
    print('----------------------- MULTADO! -----------------------')
    print('[DETRAN]: Tenha um bom dia! Dirija com segurança!')
else:
    print('[DETRAN]: Dentro dos limites permitidos!\n'
          '[DETRAN]: Tenha um bom dia! Dirija com segurança!')