# Entrada
print('Digite a idade em anos, meses e dias na ordem solicitada.')
anos = int(input('Anos: '))
meses = int(input('Meses: '))
dias = int(input('Dias: '))

# Processamento
dias_total = anos * 365  + meses * 30 + dias

# Saída
print(f'A sua idade é {dias_total} dias.')
