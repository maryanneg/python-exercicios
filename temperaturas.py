temperaturas = open('temperaturas.txt','r')
maior_temp = menor_temp = maiores = menores = maior_temp = media =0
qnt_valores = 0

for i in temperaturas.readlines():
    valores= float(temperaturas.strip())

    if valores <= 0:
        menores += 1

    if valores > 0:
        maiores +=1

    if valores < menor_temp:
        menor_temp = valores

    elif valores > maior_temp:
        maior_temp = valores
    media += valores
    qnt_valores = valores + 1

media = media / qnt_valores
file.close()
print(menor_temp)
print(maior_temp)
print(menores)
print(maiores)
print(media)

