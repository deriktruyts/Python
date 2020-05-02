n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro número inteiro: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2
divInteira = n1 // n2
restoDiv = n1 % n2

print('Valores inseridos pelo usuário: {0} e {1}\nA Soma vale: {2}\nA Subtração vale: {3}\nO Produto'
      ' vale: {4}\nA Divisão vale: {5:.3f}\nA Potência vale: {6}\nO Inteiro da Divisão vale: {7}\n'
      'O Resto da Divisão vale: {8}'.format(n1, n2, soma, subtracao, multiplicacao,
                                            divisao, potencia, divInteira, restoDiv))
