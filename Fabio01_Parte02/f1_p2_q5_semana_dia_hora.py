# Entrada
horas_entrada = int(input('Digite um valor inteiro de horas: '))

# Processamento
semanas = horas_entrada // 168
dias = (horas_entrada % 168) // 24
horas_saida = (horas_entrada % 168) % 24

# Saida
print (f'Equivale a {semanas} semanas, {dias} dias e {horas_saida} horas.')
