

#serão informados três valores referentes a X, Y e Z
def lerInteiro():
    num = int(input("Informe os dados: "))
    return num

#funções para calculo das areas
def area_triangulo_retangulo(base, altura):
    area = base * altura / 2
    return area


def area_do_circulo(raio):
    areac = PI * raio ** 2
    return areac


def trapezio_retangulo(base_maior, base_menor, altura):
    areat = ((base_maior + base_menor) * altura) / 2
    return areat

#aplicando
X = lerInteiro()
Y = lerInteiro()
Z = lerInteiro()
PI = 3.14159
print("Area do Triangulo Retangulo: "'%.2f' % area_triangulo_retangulo(X, Y))
print("Area do Circulo: "'%.2f' % area_do_circulo(Z))
print("Area do Trapezio Retangulo: "'%.2f' % trapezio_retangulo(X, Y, Z))