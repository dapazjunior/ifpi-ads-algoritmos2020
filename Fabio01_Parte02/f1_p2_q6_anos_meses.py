# Entrada
meses_totais = int(input('Digite um valor inteiro de meses: '))

# Processamento
anos = meses_totais // 12
meses_resto = meses_totais % 12

# Saida
print (f'O valor é {anos} anos e {meses_resto} meses')
