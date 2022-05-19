n=int(input('Informe número de termos na serie: '))
termo1= '1/3'
valor1 = '1'
valor2 = '3'
final= ''
resultado=0
for i in range (1,n+1):
  if i < n:
    final = final +str(i) +'/'+ str((int(valor2) * i)) + ' + '
  else:
    final = final + str(i) + '/'+ str((int(valor2) * i))
  resultado = resultado + i / (int(valor2)*i)

print(final)
print( 'Soma dos termos: ''%.2f'%resultado)