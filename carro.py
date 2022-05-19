print('Calcule as medias dos carros pesquisados')

letra = 's'
ano = 0
velocidade = 0
b = 0
a = 0
media = 0
maior = 0
menor = 0
maior1 = 0
menor1= 0
while letra in 'sS':
  letra = str(input("Aperte S para continuar ou N para finalizar: ")).strip()
  if letra in 'nN':
    break
  ano =int(input('Ano do Veiculo: '))
  velocidade = float(input('Velocidade do Veiculo: '))
  b += velocidade
  a = a +1
  media = b / a
  if a == 1:
      maior1 = menor1 = velocidade
  else:
      if velocidade > maior1:
          maior1 = velocidade
      if velocidade < menor1:
          menor1 = velocidade
  if a == 1:
      maior = menor = ano
  else:
      if ano > maior:
          maior = ano
      if ano < menor:
          menor = ano

print('A maior Velocidade: ''%.2f'%maior1)
print('O ano do carro mais novo: ''%.2f'%maior1)
print('Media das Velocidades: ''%.2f'%media)