print('Conversor de Segundos em Horas/ Minutos ')
segundos_inicial = int(input('Insira o tempo em segundos: '))
horas = segundos_inicial // (60 * 60)
minutos = segundos_inicial // 60
segundos_finais = segundos_inicial % 60
minutos_finais= minutos % 60
print('{}h {}m {}s'.format(horas,minutos_finais, segundos_finais))
