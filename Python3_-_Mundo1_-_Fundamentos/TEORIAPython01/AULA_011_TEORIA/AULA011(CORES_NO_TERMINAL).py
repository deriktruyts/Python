# CORES NO TERMINAL CORES NO TERMINAL CORES NO TERMINAL CORES NO TERMINAL CORES NO TERMINAL

# ('\033[STYLE; TEXT; BACKmOlá mundo!\033[m)

print('-=-' * 15)
print('{:=^52}'.format('\033[1m EXEMPLOS \033[m'))
print('-=-' * 15)

# Exemplo (Com todos os campos):
print('\033[0;32mExemplo\033[m com todos os campos em uso: ')
print('\033[1;30;41m SUPREME \033[m')

# Exemplo (Com somente dois campos em uso):
print('\033[0;32mExemplo\033[m com somente \033[0;33mdois\033[m campos em uso: ')
print('\033[1;30m SUPREME \033[m')

# Exemplo (Com somente um campo em uso):
print('\033[0;32mExemplo\033[m com somente \033[0;33mum\033[m campo em uso: ')
print('\033[30m SUPREME \033[m')
print('')

# =========================================================================================
# ---- STYLE ----- ---- STYLE ----- ---- STYLE ----- ---- STYLE ----- ---- STYLE ----- ---- STYLE -----
print('-=-' * 15)
print('{:=^52}'.format('\033[1m STYLE \033[m'))
print('-=-' * 15)

# 0 - Nada Nada Nada Nada Nada Nada Nada Nada Nada Nada Nada Nada Nada Nada Nada Nada Nada Nada
print('0 - Nada: ')
print('\033[0mNADA\033[m')

# 1 - Negrito Negrito Negrito Negrito Negrito Negrito Negrito Negrito Negrito Negrito Negrito Negrito
print('---' * 15)
print('1 - Negrito: ')
print('\033[1mNEGRITO\033[m')

# 4 - Sublinhado Sublinhado Sublinhado Sublinhado Sublinhado Sublinhado Sublinhado Sublinhado Sublinhado
print('---' * 15)
print('4 - Sublinhado: ')
print('\033[4mSUBLINHADO\033[m')

# 7 - Negativo (inverso) Negativo (inverso) Negativo (inverso) Negativo (inverso) Negativo (inverso) Negativo (inverso)
print('---' * 15)
print('7 - Negativo (Letra preta com\n fundo da cor escolhida): ')
print('\033[7;30mNEGATIVO\033[m')
print('')

# =========================================================================================
# ----- TEXT ----- ----- TEXT ----- ----- TEXT ----- ----- TEXT ----- ----- TEXT ----- ----- TEXT ----- ----- TEXT -----
print('-=-' * 15)
print('{:=^52}'.format('\033[1m TEXT \033[m'))
print('-=-' * 15)

# 30 - Branco Branco Branco Branco Branco Branco Branco Branco Branco Branco Branco Branco Branco
print('30 - Branco: ')
print('\033[30mBRANCO\033[m')

# 31 - Vermelho Vermelho Vermelho Vermelho Vermelho Vermelho Vermelho Vermelho Vermelho Vermelho
print('---' * 15)
print('31 - Vermelho: ')
print('\033[31mVERMELHO\033[m')

# 32 - Verde Verde Verde Verde Verde Verde Verde Verde Verde Verde Verde Verde Verde Verde Verde
print('---' * 15)
print('32 - Verde: ')
print('\033[32mVERDE\033[m')

# 33 - Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo
print('---' * 15)
print('33 - Amarelo: ')
print('\033[33mAMARELO\033[m')

# 34 - Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul
print('---' * 15)
print('34 - Azul: ')
print('\033[34mAZUL\033[m')

# 35 - Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo
print('---' * 15)
print('35 - Roxo: ')
print('\033[35mROXO\033[m')

# 36 - Azul bebê Azul bebê Azul bebê Azul bebê Azul bebê Azul bebê Azul bebê Azul bebê Azul bebê Azul bebê
print('---' * 15)
print('36 - Azul bebê: ')
print('\033[36mAZUL BEBÊ\033[m')

# 37 - Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza
print('---' * 15)
print('37 - Cinza: ')
print('\033[37mCINZA\033[m')
print('')

# =========================================================================================
# ----- BACK ----- ----- BACK ----- ----- BACK ----- ----- BACK ----- ----- BACK ----- ----- BACK -----
print('-=-' * 15)
print('{:=^52}'.format('\033[1m BACK \033[m'))
print('-=-' * 15)

# 40 - Branco Branco Branco Branco Branco Branco Branco Branco Branco Branco Branco Branco Branco
print('40 - Branco: ')
print('\033[1;31;40mBRANCO\033[m')

# 41 - Vermelho Vermelho Vermelho Vermelho Vermelho Vermelho Vermelho Vermelho Vermelho Vermelho
print('41 - Vermelho: ')
print('\033[1;30;41mVERMELHO\033[m')

# 42 - Verde Verde Verde Verde Verde Verde Verde Verde Verde Verde Verde Verde Verde Verde Verde
print('42 - Verde: ')
print('\033[1;30;42mVERDE\033[m')

# 43 - Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo Amarelo
print('43 - Amarelo: ')
print('\033[1;30;43mAMARELO\033[m')

# 44 - Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul Azul
print('44 - Azul: ')
print('\033[1;30;44mAZUL\033[m')

# 45 - Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo Roxo
print('45 - ROXO: ')
print('\033[1;30;45mROXO\033[m')

# 46 - Azul bebê Azul bebê Azul bebê Azul bebê Azul bebê Azul bebê Azul bebê Azul bebê Azul bebê Azul bebê
print('46 - Azul bebê: ')
print('\033[1;30;46mAZUL BEBÊ\033[m')

# 47 - Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza Cinza
print('47 - Cinza: ')
print('\033[1;30;47mCINZA\033[m')
print('')
print('-=-' * 15)