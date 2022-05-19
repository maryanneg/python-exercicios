print('Simulação de Aluguel')

tipo_aluguel = input("Tipo de Aluguel (PREMIUM/STANDARD): ").strip()
dias_aluguel = int(input('Quantos dias de aluguel? '))
dias_Tv = int(input('Quantos dias de utilização da TV? '))
dias_internet = int(input('Quantos Dias de utilização da Internet? '))

if tipo_aluguel == 'PREMIUM':
    premium = 200
    valor_a = premium * dias_aluguel
elif tipo_aluguel == 'STANDARD':
    standard = 150
    valor_a = standard * dias_aluguel

if dias_Tv > 0:
      tv = 10
      valor_b = tv * dias_Tv
else:
    valor_b = 0

if dias_internet > 0:
    internet = 15
    valor_c = internet * dias_internet
else: valor_c = 0

valor_Total = valor_a + valor_b + valor_c
print ('Você pagará o valor total de: ''%.2f' % valor_Total)