# Entrada
anos = int(input('Há quantos anos você fuma? '))
cigarros_diario = int(input('Quantos cigarros fuma por dia? '))
valor_carteira = int(input('Qual o valor da carteira? '))

# Processamento
from math import ceil
cigarros_totais = anos * 365 * cigarros_diario
total_carteiras = ceil(cigarros_totais / 20)
gasto = total_carteiras * valor_carteira

# Saída
print (f'Você gastou R$ {gasto:.2f} com cigarros.')
