# Entrada
minutos_entrada = int(input('Digite um valor em minutos: '))

# Processamento
horas = minutos_entrada // 60
minutos_saida = minutos_entrada % 60

# Saída
print(f'O resultado é {horas} horas e {minutos_saida} minutos')
