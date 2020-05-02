''' tempo = int(input('Insira (em números) a quantos anos você possui seu carro: '))

if tempo <=3:
    print('Seu carro está novo!')
else:
    print('Seu carro está velho.')
print('{:=^20}'.format('Fim')) '''

# -----------------------------------------------------------------------------------
# É possível realizar este comando acima em apenas três linhas:
# -----------------------------------------------------------------------------------

''' tempo = int(input('Insira (em números) a quantos anos você possui seu carro: '))
print('Seu carro está novo!'if tempo <=3 else print('Seu carro está velho.'))
print('{:=^20}'.format('Fim')) '''

# -----------------------------------------------------------------------------------
# Praticando um pouco mais:
# -----------------------------------------------------------------------------------

''' nome = input('Insira seu primeiro nome: ')
if nome == 'Bianca':
    print('Que lindo nome você tem!')
elif nome == 'Derik':
    print('Que lindo nome você tem!')
else:
    print('Seu nome é muito comum.')
print('Bom dia, {}!'.format(nome)) '''

# -----------------------------------------------------------------------------------
# Praticando um pouco mais:
# -----------------------------------------------------------------------------------

''' n1 = float(input('Insira sua A1: '))
n2 = float(input('Insira sua D1: '))
n3 = float(input('Insira sua A2: '))
n4 = float(input('Insira sua D2: '))
n5 = float(input('Insira sua D3: '))

nf = (n1 + n2 + n3 + n4 + n5)

if nf >= 70.0:
    print('APROVADO!')
else:
    print('REPROVADO!') '''