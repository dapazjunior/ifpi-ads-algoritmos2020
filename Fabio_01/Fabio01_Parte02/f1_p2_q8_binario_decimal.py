#  Entrada
numero = int(input('Digite um numero inteiro (binário) de 4 algarismos: '))

# Processamento
digito3 = numero // 1000
digito2 = (numero % 1000) // 100
digito1 = ((numero % 1000) % 100) // 10
digito0 = ((numero % 1000) % 100) % 10
decimal = digito0 * 2**0 + digito1 * 2**1 + digito2 * 2**2 + digito3 * 2**3

# Saída
print(f'Esse número em  decimal é {decimal}.')
