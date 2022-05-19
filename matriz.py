def matriz_m (m_l,n_c):
    return [[i*j for j in range(n_c)] for i in range(m_l)]
m_l = int(input('Informe quantidade de linhas: '))
n_c = int(input('Informe quantidade de colunas: '))
matriz = matriz_m(m_l,n_c)
print(matriz)