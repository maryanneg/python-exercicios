def histograma(palavra):

  dicionario = {}
  for letra in palavra:
    contagem = dicionario.get(palavra,0)
    contagem += 1
    dicionario[palavra] = contagem


  return dicionario

if __name__ == '__main__':
  palavra_usuario = input("Informe uma palavra: ")
  print(histograma(palavra_usuario ))
  print()
