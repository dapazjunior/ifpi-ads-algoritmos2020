#  Entrada
numero = int(input('Digite um numero inteiro de 4 algarismos: '))

# Processamento
unidade_milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = ((numero % 1000) % 100) // 10
unidade = ((numero % 1000) % 100) % 10
soma_algarismos = unidade_milhar + centena + dezena + unidade

# Saída
print(f'A soma dos algarismos desse número é: {soma_algarismos}.')
