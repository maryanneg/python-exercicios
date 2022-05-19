#seq_ord = input().strip()
#valor = seq_ord.find('1')
#print(valor)
numero=int(input('Digite o valor para aplicar o padrão: '))
while numero > 0:
    for num in range(1, numero + 1):
        linha = ""
    for i in range(0, num):
        linha += str(num) + ' '
    print(linha)
    break