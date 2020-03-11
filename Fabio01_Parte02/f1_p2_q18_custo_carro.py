# Entrada
custo_fabrica = float(input('Qual o custo de fábrica do carro? '))

# Processamento
custo_distribuidor = custo_fabrica * 0.28
custo_imposto = custo_fabrica * 0.45
custo_consumidor = custo_fabrica + custo_distribuidor + custo_imposto

# Saída
print(f'O custo do carro para o consumidor é R$ {custo_consumidor:.2f}.')
