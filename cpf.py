def maior(grupo):
    lista = []
    lista.append(int(grupo[0]))
    lista.append(int(grupo[1]))
    lista.append(int(grupo[2]))
    return max(lista)


cpf = ''

while True:
    soma = 0
    digitos = input('Digite o Valor do seu CPF: ').strip()

    if digitos == 'FIM':
        break
    cpf = digitos.split('.')

    for i in range(len(cpf)):

        if '-' not in cpf[i]:
            soma = soma + maior(cpf[i])
        else:
            soma = soma + maior(cpf[i].replace('-', ''))
    if (soma % 10 == int(digitos[-1:])):
        print('VALIDO')
    else:
        print('INVALIDO')

