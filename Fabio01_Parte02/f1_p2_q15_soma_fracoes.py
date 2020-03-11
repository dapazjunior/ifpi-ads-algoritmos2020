# Entrada
numerador1 = int(input('Digite o numerador da primeira fração: '))
denominador1 = int(input('Digite o denominador da primeira fração: '))
numerador2 = int(input('Digite o numerador da segunda fração: '))
denominador2 = int(input('Digite o denominador da segunda fração: '))

# Processamento
denominador = denominador1 * denominador2
numerador = (denominador // denominador1)*numerador1 + (denominador // denominador2)*numerador2

# Saída
print(f'A soma desses números é {numerador}/{denominador}.')
