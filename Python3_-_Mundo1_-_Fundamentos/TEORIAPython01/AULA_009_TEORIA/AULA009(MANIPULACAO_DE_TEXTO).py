frase = 'Curso em Vídeo Python'

# C = 0
# n = 20

print('------------------------')

print('FRASE:')
print(frase)
print('||||||||||..........|')
print('0123456789..........20')

print('------------------------')  # len
print('Comprimento da frase:', len(frase), 'caracteres (-1)')
print('------------------------')  # count
print('Quantidade de letra "o" na frase inteira:', frase.count('o'))
print('Quantidade de letra "o" do 0 até a casa 14:', frase.count('o', 0, 14))
print('------------------------')  # find
print('Em qual casa é encontrado o início da palavra "deo" na frase inteira:', frase.find('deo'))
print('------------------------')  # in
print('Existe a palavra "Curso" na frase?', ('Curso' in frase))
print('------------------------')  # replace
print('Troque a palavra "Python" por "BiancaLinda":', frase.replace('Python', 'BiancaLinda'))
print('------------------------')

print('[9:13]: ' + frase[9:13])  # Irá printar "Víde", sem a letra "o"

print('[9:14]: ' + frase[9:14])  # Irá printar "Vídeo"

print('[9:21]: ' + frase[9:21])  # Irá printar "Vídeo Python", sendo V = 9 e n = 20,
                                 #desconsiderendo a casa 21.

print('[9:21:2]: ' + frase[9:21:2])  # Irá printar "VdoPto", pois irá pular de 2 em 2.

print('[:5]: ' + frase[:5])  # Irá printar do início (pois a casa inicial não foi declarada)
                             #até a quinta(-1) casa da frase.

print('[15:]: ' + frase[15:])  # Irá printar a partir do 15 até o final.

print('[9::3]: ' + frase[9::3])  # Irá printar a partir do nove, até o final, pulando de 3 em 3