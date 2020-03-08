#  Entrada
numero = int(input('Digite um numero inteiro de 3 algarismos: '))

# Processamento
centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10
inverso = unidade * 100 + dezena * 10 + centena

# Saida
print(f'O inverso é {inverso}.')
