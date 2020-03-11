# Entrada
print('Digite a idade em anos, meses e dias na ordem solicitada.')
dias_totais = int(input('Digite a idade em quantidade de dias: '))

# Processamento
anos = dias_totais // 365
meses = (dias_totais % 365) // 30
dias = (dias_totais % 365) % 30

# Saída
print(f'A sua idade é {anos} anos, {meses} meses e {dias} dias.')
