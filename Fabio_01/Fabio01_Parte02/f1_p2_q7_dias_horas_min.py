# Entrada
minutos_entrada = int(input('Digite um valor inteiro de minutos: '))

# Processamento
dias = minutos_entrada // 1440
horas = (minutos_entrada % 1440) // 60
minutos_saida = (minutos_entrada % 1440) % 60

# Saida
print (f'Equivale a {dias} dias, {horas} horas e {minutos_saida} minutos.')
