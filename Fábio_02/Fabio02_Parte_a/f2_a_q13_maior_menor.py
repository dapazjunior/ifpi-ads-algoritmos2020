def main():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    num3 = int(input('Digite o terceiro número: '))
    num4 = int(input('Digite o quarto número: '))
    num5 = int(input('Digite o quinto número: '))
    
    maior = verificar_maior(num1, num2, num3, num4, num5)
    
    menor = verificar_menor(num1, num2, num3, num4, num5)
    
    print(f'O maior número é {maior} e o menor é {menor}')


def verificar_maior(num1, num2, num3, num4, num5):
    maior = num1
    if num2 > maior:
        maior = num2
    if num3 > maior:
        maior = num3
    if num4 > maior:
        maior = num4
    if num5 > maior:
        maior = num5
    return maior
    

def verificar_menor(num1, num2, num3, num4, num5):
    menor = num1
    if num2 < menor:
        menor = num1
    if num3 < menor:
        menor = num3
    if num4 < menor:
        menor = num4
    if num5 < menor:
        menor = num5
    return menor


main()
