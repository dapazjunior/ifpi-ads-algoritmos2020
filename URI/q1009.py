nome = input()
salario = float(input())
vendas = float(input())
salario = salario + 0.15 * vendas

print('TOTAL = R$ {:.2f}'.format(salario))