lado_a= int(input('Informe o lado A do triangulo: '))
lado_b= int(input('Informe o lado B triangulo: '))
lado_c= int(input('Informe o lado C triangulo: '))

if lado_a == lado_b and lado_a == lado_c:
    print('equilatero')

elif lado_a != lado_b and lado_a != lado_c:
    print('escaleno')
else:
    print('isosceles')