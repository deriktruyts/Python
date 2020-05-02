from time import sleep

print('\033[31m[HENRI]\033[m: Olá! Eu sou o Henri, o neném recém-nascido. E estou aqui para conversar com você!')
sleep(1)

print('\033[31m[HENRI]\033[m: Antes de começarmos, por favor me diga seu nome completo, seu gênero e sua idade :3')
sleep(1)

nome = input('\033[33m • \033[mNome completo:\n')
sexo = input('\033[33m • \033[mGênero:\n')
idade = int(input('\033[33m • \033[mIdade:\n'))

# IDADE # IDADE # IDADE # IDADE # IDADE # IDADE # IDADE # IDADE # IDADE # IDADE # IDADE # IDADE # IDADE # IDADE # IDADE

listar = nome.split()
if sexo == \
        'Masculino' \
        or sexo == 'masculino' \
        or sexo == 'M' \
        or sexo == 'm' \
        or sexo == 'Masc' \
        or sexo == 'masc'\
        or sexo == 'Homem'\
        or sexo == 'homem':
    print('\033[31m[HENRI]\033[m: Olá, seja muito bem vindo, {}!'.format(listar[0]))
elif sexo == \
        'Feminino' \
        or sexo == 'feminino' \
        or sexo == 'F' \
        or sexo == 'f' \
        or sexo == 'Fem' \
        or sexo == 'fem'\
        or sexo == 'Mulher'\
        or sexo == 'mulher':
    print('\033[31m[HENRI]\033[m: Olá, seja muito bem vinda, {}!'.format(listar[0]))
else:
    print('\033[31m[HENRI]\033[m: Olá, seja muito bem vindo(a), {}!'.format(listar[0]))
sleep(2)
# NOMES COMUNS # NOMES COMUNS # NOMES COMUNS # NOMES COMUNS # NOMES COMUNS # NOMES COMUNS # NOMES COMUNS # NOMES COMUNS
if listar[len(listar)-1] == 'Silva' \
        or listar[len(listar)-1] == 'Souza' \
        or listar[len(listar)-1] == 'Ferreira' \
        or listar[len(listar) - 1] == 'Costa' \
        or listar[len(listar)-1] == 'Oliveira' \
        or listar[len(listar)-1] == 'Pereira' \
        or listar[len(listar) - 1] == 'Rodrigues':
    print('\033[31m[HENRI]\033[m: Seu sobrenome é muito popular no Brasil!! {}!'.format(listar[len(listar)-1]))
elif listar[len(listar)-1] == 'Truyts' \
        or listar[len(listar)-1] == 'truyts' \
        or listar[len(listar)-1] == 'TRUYTS':
    print('\033[31m[HENRI]\033[m: Iupiiiii!!! Você é um Truyts!')
elif listar[len(listar)-1] == 'Brocaldi' \
        or listar[len(listar)-1] == 'brocaldi' \
        or listar[len(listar)-1] == 'BROCALDI' \
        or listar[len(listar)-1] == 'Martins':
    print('\033[31m[HENRI]\033[m:Que legal!! Você é da família da namorada do meu tio, né?!')
else:
    print('\033[31m[HENRI]\033[m: Que lindo sobrenome! {}!'.format(listar[len(listar)-1]))
sleep(2)
# SIM # SIM # SIM # SIM # SIM # SIM # SIM # SIM # SIM # SIM # SIM # SIM # SIM # SIM # SIM # SIM # SIM # SIM # SIM
papo = input('\033[31m[HENRI]\033[m: O que acha de batermos um papo, {}?\n'.format(listar[0]))
if papo == 'Sim' or papo == 'sim' or papo == 'S' or papo == 's' or papo == 'Si' or papo == 'si' or papo == 'Vamos'\
        or papo == 'vamos' or papo == 'Vamo' or papo == 'vamo' or papo == 'Bora' or papo == 'bora' or papo == 'Legal'\
        or papo == 'legal' or papo == 'Legal, vamos' or papo == 'legal, vamos' or papo == 'Legal vamos' \
        or papo == 'legal vamos':
    sleep(2)
    print('\033[31m[HENRI]\033[m: Uhuuu! Eu começo!!')
    sleep(2)
    perg1: str = input('\033[31m[HENRI]\033[m: Me conte um pouco sobre você!! O que você gosta de fazer?\n')
    texto = ('o'*20)
    if len(perg1) >= len(texto):
        sleep(2)
        print('\033[31m[HENRI]\033[m: Que interessante!!! Sua vida parece ser muito agitada!')
    else:
        sleep(2)
        print('\033[31m[HENRI]\033[m: Legal! Porém acredito que você pode melhorar sua produtividade no dia a dia!')
        sleep(4)
        print('\033[31m[HENRI]\033[m: Aqui vai uma lista de coisas para fazer durante seu dia: \n'
              '\033[33m • \033[mAnde na natureza;\n'
              '\033[33m • \033[mBrinque com o seu animal de estimação;\n'
              '\033[33m • \033[mPesquise por coisas nostalgicas;\n'
              '\033[33m • \033[mSeja um voluntário;\n'
              '\033[33m • \033[mDescubra-se na cozinha;\n'
              '\033[33m • \033[mTente uma nova aula de exercícios;\n'
              '\033[33m • \033[mEscreva em um diário;\n'
              '\033[33m • \033[mVá em um museu.')
# NÃO # NÃO # NÃO # NÃO # NÃO # NÃO # NÃO # NÃO # NÃO # NÃO # NÃO # NÃO # NÃO # NÃO # NÃO # NÃO # NÃO # NÃO # NÃO
elif papo == 'Não' or papo == 'não' or papo == 'Nao' or papo == 'nao' or papo == 'N' or papo == 'n' or papo == 'Nã' \
        or papo == 'nã' or papo == 'Na' or papo == 'na' or papo == '' or papo == '' or papo == '' or papo == '':
    Nao = input('\033[31m[HENRI]\033[m: Buaaaaá! Você não gosta de mim?\n')
    if Nao == 'Gosto' or Nao == 'gosto' or Nao == 'Eu gosto' or Nao == 'eu gosto' or Nao == 'Eu gosto sim' \
            or Nao == 'eu gosto sim' or Nao == 'Eu gosto de você' \
            or Nao == 'eu gosto de você' or Nao == 'Eu gosto de voce' or Nao == 'eu gosto de voce' \
            or Nao == 'Eu gosto de vc' or Nao == 'eu gosto de vc' or Nao == 'Eu amo você' or Nao == 'eu amo você' \
            or Nao == 'Eu amo vc' or Nao == '' or Nao == 'eu amo vc' or Nao == 'Eu te amo, Henri' \
            or Nao == 'eu te amo, Henri' or Nao == 'Eu te amo Henri' or Nao == 'eu te amo Henri' \
            or Nao == 'Eu te amo henri' or Nao == 'eu te amo henri':
        sleep(2)
        print('\033[31m[HENRI]\033[m: Ebaaa!! Então vamos continuar o papo...')
        sleep(2)
    pergu1: str = input('\033[31m[HENRI]\033[m: Me conte um pouco sobre você!! O que você gosta de fazer?\n')
    texto = ('o'*20)
    if len(pergu1) >= len(texto):
        sleep(2)
        print('\033[31m[HENRI]\033[m: Que interessante!!! Sua vida parece ser muito agitada!')
    else:
        sleep(2)
        print('\033[31m[HENRI]\033[m: Legal! Porém acredito que você pode melhorar sua produtividade no dia a dia!')
        sleep(2)
        print('\033[31m[HENRI]\033[m: Aqui vai uma lista de coisas para fazer durante seu dia: \n'
              '\033[33m • \033[mAnde na natureza;\n'
              '\033[33m • \033[mBrinque com o seu animal de estimação;\n'
              '\033[33m • \033[mPesquise por coisas nostalgicas;\n'
              '\033[33m • \033[mSeja um voluntário;\n'
              '\033[33m • \033[mDescubra-se na cozinha;\n'
              '\033[33m • \033[mTente uma nova aula de exercícios;\n'
              '\033[33m • \033[mEscreva em um diário;\n'
              '\033[33m • \033[mVá em um museu.')
else:
    print('\033[31m[HENRI]\033[m: Ok! Você não quer papo, eu entendo. Tudo bem, até mais tarde!')
sleep(2)
print('\033[31m[HENRI]\033[m: Mudando de assunto agora...')
if 0 <= idade < 4 and sexo == 'Masculino':
    print('\033[31m[HENRI]\033[m: Que incrível!!! Um neném! assim como eu :3')
elif 0 <= idade < 4 and sexo == 'Feminino':
    print('\033[31m[HENRI]\033[m: Percebi que você é uma neném, assim como eu :3')
elif 4 <= idade < 14 and sexo == 'Masculino':
    print('\033[31m[HENRI]\033[m: Percebi que você é um pouco mais velho do que eu :3')
elif 4 <= idade < 14 and sexo == 'Feminino':
    print('\033[31m[HENRI]\033[m: Percebi que você é um pouco mais velha do que eu :3')
elif 14 <= idade < 26 and sexo == 'Masculino':
    print('\033[31m[HENRI]\033[m: Percebi que você já é muito grandinho pra falar comigo, '
          'mas tudo bem. Estou aqui para todos!!')
elif 14 <= idade < 26 and sexo == 'Feminino':
    print('\033[31m[HENRI]\033[m: Percebi que você já é muito grandinha pra falar comigo, '
          'mas tudo bem. Estou aqui para todos!!')
elif 26 <= idade < 70 and sexo == 'Masculino':
    print('\033[31m[HENRI]\033[m: Percebi que você já é um adulto! '
          'Nem imagino como deve ser!')
elif 26 <= idade < 70 and sexo == 'Feminino':
    print('\033[31m[HENRI]\033[m: Percebi que você já é uma adulta! '
          'Nem imagino como deve ser!')
elif 70 <= idade <= 150 and sexo == 'Masculino':
    print('\033[31m[HENRI]\033[m: Percebi que você já é um senhorzinho!!')
elif 70 <= idade <= 150 and sexo == 'Feminino':
    print('\033[31m[HENRI]\033[m: Percebi que você já é uma senhorinha!!')
else:
    print('\033[31m[HENRI]\033[m: Não identifiquei sua idade, seu estranho')
sleep(2)
if idade > 3:
    pergu2 = input('\033[31m[HENRI]\033[m: Como é ter {} anos?'.format(idade))
else:
    print('\033[31m[HENRI]\033[m: Você não deveria nem saber escrever com a sua idade!! Quem diria saber digitar :?')
print('Puxa vida!!! Deve ser muito legal ter a sua idade!! Mas eu prefiro ser um bebê, sem muitas complicações :P')
