def main():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    num3 = int(input('Digite o terceiro número: '))
    
    maior = verificar_maior(num1, num2, num3)
    
    print(f'O maior número digitado é {maior}.')
    


def verificar_maior(num1, num2, num3):
    maior = num1
    if num2 >= maior:
        maior = num2
        return maior
    elif num3 >= maior:
        maior = num3
        return maior
    else:
        return maior


main()
