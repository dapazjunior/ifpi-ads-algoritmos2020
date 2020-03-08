# Entrada
numero = int(input('Digite um numero inteiro de 3 algarismos: '))

# Processamento
centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10
soma = centena + dezena + unidade

# Saida
print(f'A soma dos algarismos é {soma}.')
