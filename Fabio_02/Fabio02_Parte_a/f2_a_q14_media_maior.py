def main():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    num3 = int(input('Digite o terceiro número: '))
    num4 = int(input('Digite o quarto número: '))
    num5 = int(input('Digite o quinto número: '))
    
    media = calcular_media(num1, num2, num3, num4, num5)
         
    print(f'A média desses números é {media} e os números maiores que a média são: ')
    
    verificar_se_maior(num1, num2, num3, num4, num5, media)
    
    


def calcular_media(num1, num2, num3, num4, num5):
    media = (num5 + num2 + num3 + num4 + num5) / 5
    return media


def verificar_se_maior(num1, num2, num3, num4, num5, media):
    if num1 > media:
        print(f'{num1}')
    if num2 > media:
        print(f'{num2}')
    if num3 > media:
        print(f'{num3}')
    if num4 > media:
        print(f'{num4}')
    if num5 > media:
        print(f'{num5}') 


main()
