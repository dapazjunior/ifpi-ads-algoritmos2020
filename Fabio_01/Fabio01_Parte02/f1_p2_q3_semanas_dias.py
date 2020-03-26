# Entrada
dias_totais = int(input('Digite um valor inteiro de dias: '))

# Processamento
semana = dias_totais // 7
dias_resto = dias_totais % 7

# Saida
print (f'O valor é {semana} semanas e {dias_resto} dias')
