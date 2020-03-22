def main():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    num3 = int(input('Digite o terceiro número: '))
    
    igual = verificar_iguais(num1, num2, num3)
    
    print(f'Você digitou {igual} número(s) iguais.')
    


def verificar_iguais(num1, num2, num3):
    if(num1 == num2 == num3):
        return 3
    elif((num1 == num2 and num1 != num3) or (num1 == num3 and num1 != num2) or (num2 == num3 and num1 != num2)):
        return 2
    else:
        return 0


main()
