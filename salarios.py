
salario = float(input('Informe o valor do salario: '))

if (salario <= 280):
    percentual = 20
elif (salario <= 700):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5

print('Salário atual: ''%.2f'% salario)
print( 'Percentual de aumento em % é de: ' '{}% '.format(percentual))

percentual = percentual / 100.0
aumento = percentual * salario
novo_salario = salario + aumento

print('Aumento de R$: ' '%.2f'% aumento)
print('Novo Salário: ' '%.2f'% novo_salario)