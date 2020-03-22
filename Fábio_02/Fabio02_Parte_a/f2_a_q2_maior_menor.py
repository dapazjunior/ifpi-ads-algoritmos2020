def main():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite outro número, diferente do primeiro: '))
    
    maior = verificar_maior(num1, num2)
    if maior == True:
        print(f'O maior número é {num1}, e o menor é {num2}.')
    else:
        print(f'O maior número é {num2}, e o menor é {num1}')


def verificar_maior(num1, num2):
    a = num1 > num2
    return a

main()
