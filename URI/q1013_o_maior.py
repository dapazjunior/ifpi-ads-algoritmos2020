def main():
    num1, num2, num3 = input().split(' ')
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    
    maior = verificar_maior(num1, num2, num3)
    
    print(f'{maior} eh o maior')
    


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
