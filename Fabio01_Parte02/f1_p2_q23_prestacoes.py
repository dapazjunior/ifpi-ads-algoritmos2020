# Entrada
valor = float(input('Qual o valor do produto? '))

# Processamento
prestacao = valor // 3
entrada = (valor // 3) + (valor % 3)

# Saída
print(f'O pagamento será uma entrada de R$ {entrada:.2f} e mais duas prestações de R$ {prestacao:.2f}.')
