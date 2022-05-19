
#organização de inteiros em ordem crescente
n1 = int(input('Informe o primeiro digito: '))
n2 = int(input('Informe o segundo digito: '))
n3 = int(input('Informe o terceiro digito: '))
if n1 < n2 < n3:
    print(f'{n1} \n{n2}\n{n3}')
if n1 < n3 < n2:
    print(f'{n1}\n{n3}\n{n2}')
if n2 < n1 < n3:
    print(f'{n2}\n{n1}\n{n3}')
if n2 < n3 < n1:
    print(f'{n2}\n{n3}\n{n1}')
if n3 < n2 < n1:
    print(f'{n3}\n{n2}\n{n1}')
if n3 < n1 < n2:
    print(f'{n3}\n{n1}\n{n2}')