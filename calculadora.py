#calculos\\\
def media_a():
    num = []
    qnt_num = int(input('Quantidade de valores inteiros:'))
    for i in range (0,qnt_num):
      num += [int(input('Valor: '))]
    soma = 0
    for i in num:
      soma += i
    media = soma / qnt_num
    print('Média aritmética = ' '%.2f'% media)
    menu()
def media_p():
    num2 = []
    pesos = []
    multi = []
    qnt_num = int(input('Quantidade de valores inteiros: '))
    for i in range (0,qnt_num):
      num2+= [int(input('Valor: '))]
      pesos += [int(input('Peso: '))]
    for valores, valores_pesos in zip(num2,pesos):
      multi.append(valores * valores_pesos)
    soma_p = 0
    for i in pesos:
      soma_p += i
    soma_m = 0
    for i in multi:
      soma_m += i
    media_ponderada = soma_m / soma_p
    print('Média ponderada = ''%.2f'%media_ponderada)
    menu()
def juros_s():
  valor = int(input('Valor inicial: '))
  taxa = int(input('Taxa de juros por mês: ')) / 100
  tempo = int(input('Tempo do empréstimo: '))
  juros = valor * taxa * tempo
  print('Juro Simples = R$: ''%.0f' % juros)
  menu()
def juros_c():
  valor = int(input('Valor inicial: '))
  taxa = int(input('Taxa de juros por mês: ')) / 100
  tempo = int(input('Tempo do empréstimo: '))
  montante = valor * (1 + taxa) ** tempo
  juros_composto = montante - valor
  print('Juro Composto = R$: ''%.0f' % juros_composto)
  menu()


#menu\\\
def menu():
  print('Calculadora')
  print('1 - Calcular a média aritmética; \n2 - Calcular a média ponderada; \n3 - Calcular os juros simples ao mês;\n4 - Calcular os juros compostos ao mês;\n0 - Sair do programa.')
menu()
op_menu = int(input('Digite o número da opção (1, 2, 3 ou 4) ou 0 para sair\n'))

#execução \\\
while op_menu != 0:
  if op_menu == 1:
    media_a()
    op_menu = int(input('Digite o número da opção (1, 2, 3 ou 4) ou 0 para sair\n'))
  if op_menu == 2:
    media_p()
    op_menu = int(input('Digite o número da opção (1, 2, 3 ou 4) ou 0 para sair\n'))
  if op_menu == 3:
    juros_s()
    op_menu = int(input('Digite o número da opção (1, 2, 3 ou 4) ou 0 para sair\n'))
  if op_menu == 4:
    juros_c()
    op_menu = int(input('Digite o número da opção (1, 2, 3 ou 4) ou 0 para sair\n'))
