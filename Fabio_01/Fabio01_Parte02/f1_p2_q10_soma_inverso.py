#  Entrada
numero = int(input('Digite um numero inteiro de 3 algarismos: '))

# Processamento
centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10
inverso = unidade * 100 + dezena * 10 + centena
soma = numero + inverso

# Saida
print(f'A diferença entre esse número e seu inverso é {soma}.')
