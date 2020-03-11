# Entrada
valor = int(input('Quanto deseja sacar? '))

# Processamento
cem = valor // 100
resto = valor % 100

cinquenta = resto // 50
resto = resto % 50

vinte = resto // 20
resto = resto % 20

dez = resto // 10
resto = resto % 10

cinco = resto // 5
resto = resto % 5

dois = resto // 2
resto = resto % 2

saque = valor - resto

# Saída
print(f'As cédulas permitem sacar R$ {saque:.2f}.')
print(f'{cem} x R$ 100,00 \n{cinquenta} x R$ 50,00 \n{vinte} x R$ 20,00 \n{dez} x R$ 10,00 \n{cinco} x R$ 5,00 \n{dois} x R$ 2,00 \n********************************* ')
