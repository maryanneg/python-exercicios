sexo = input('Gênero (F/M): ')
altura = float(input("Altura: "))
pesoAtual = float(input("Peso: "))


def exit():
    if pesoAtual > pesoIdeal:
        print('acima do peso')
    elif pesoAtual < pesoIdeal:
        print('abaixo do peso')
    elif pesoAtual == pesoIdeal:
        print('ideal')


if sexo == 'M':
    pesoIdeal = (72.7 * altura) - 58

    exit()

elif sexo == 'F':
    pesoIdeal = (62.1 * altura) - 44.7

    exit()