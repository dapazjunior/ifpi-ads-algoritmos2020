# Entrada
valor_m_inicial = int(input('Digite um valor inteiro em m: '))

# Processamento
valor_km = valor_m_inicial // 1000
valor_m_final = valor_m_inicial % 1000

# Saida
print (f'O valor é {valor_km} km e {valor_m_final} m')
