# EXEMPLOS DE COMO DEIXAR UM TEXTO AJUSTADO DENTRO DE UMA MÁSCARA
# ---------------------------------------------------------------
# SEM AJUSTE:
nome = input('Insira seu nome (SEM AJUSTE): ')
print('Seja muito bem-vindo, {}!'.format(nome))
print('')
# ---------------------------------------------------------------
# COM AJUSTE PARA DIREITA:
nome = input('Insira seu nome (COM AJUSTE PARA DIREITA): ')
print('Seja muito bem-vindo, {:>20}!'.format(nome))
print('')
# ---------------------------------------------------------------
# COM AJUSTE PARA ESQUERDA:
nome = input('Insira seu nome (COM AJUSTE PARA ESQUERDA): ')
print('Seja muito bem-vindo, {:<20}!'.format(nome))
print('')
# ---------------------------------------------------------------
# COM AJUSTE CENTRALIZADO:
nome = input('Insira seu nome (COM AJUSTE CENTRALIZADO): ')
print('Seja muito bem-vindo, {:^20}!'.format(nome))
print('')
# ---------------------------------------------------------------
# COM AJUSTE DE CARACTERES EM VOLTA CENTRALIZADO:
nome = input('Insira seu nome (COM AJUSTE DE CARACTERES EM VOLTA CENTRALIZADO): ')
print('Seja muito bem-vindo, {:=^20}!'.format(nome))
