n1 = float(input('PRIMEIRA NOTA: '))
n2 = float(input('SEGUNDA NOTA: '))
media = (n1 + n2) / 2

if media == 10.0:
    print('Média: ''%.1f' % media, '\nAprovado com Distinção')

if media >=7 and media <= 9.9:
    print('Média: ''%.1f' % media, '\nAprovado')

if media < 7:
    print('Média: ''%.1f' % media,'\nReprovado')
