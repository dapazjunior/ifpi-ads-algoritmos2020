# Entrada
segundos_entrada = int(input('Digite um valor inteiro de segundos: '))

# Processamento
horas = segundos_entrada // 3600
minutos = (segundos_entrada % 3600) // 60
segundos_saida = (segundos_entrada % 3600) % 60

# Saida
print (f'Equivale a {horas} horas, {minutos} minutos e {segundos_saida} segundos.')
