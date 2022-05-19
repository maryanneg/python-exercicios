genero = (input())
altura = float(input())
peso = float(input())

if genero =='M':
    peso_idealM = (72.7 * altura) - 58
    if peso == peso_idealM:
        print('ideal')
    elif peso > peso_idealM:
        print('acima do peso')
    if peso < peso_idealM:
        print('abaixo do peso')

else:
    peso_idealF = (62.1 * altura) - 44.7
    if peso == peso_idealF:
        print('ideal')
    elif peso > peso_idealF:
        print('acima do peso')
    if peso < peso_idealF:
        print('abaixo do peso')







