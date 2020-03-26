# Entrada
nota_1 = float(input('Digite a primeira nota: '))
peso_1 = float(input('Digite o peso da primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
peso_2 = float(input('Digite o peso da segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))
peso_3 = float(input('Digite o peso da terceira nota: '))

# Processamento
media = (nota_1 * peso_1 + nota_2 * peso_2 + nota_3 * peso_3)/(peso_1 + peso_2 + peso_3)

# Saida
print(f'A media das notas é {media:.2f}.')
