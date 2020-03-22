def main():
    lado1 = int(input('Digite a medida do primeiro lado: '))
    lado2 = int(input('Digite a medida do segundo lado: '))
    lado3 = int(input('Digite a medida do terceiro lado: '))
    
    eh_triangulo = verificar_se_triangulo(lado1, lado2, lado3)
    
    if eh_triangulo == True:
        verificar_se_retangulo(lado1, lado2, lado3)
    else:
        print('As medidas não formam um triângulo.')
   
def verificar_se_triangulo(lado1, lado2, lado3):
    if (lado1 < (lado2 + lado3)) and (lado2 < (lado1 + lado3)) and (lado3 < (lado1 + lado2)):
        return True
    else:
        return False


def verificar_se_retangulo(lado1, lado2, lado3):
    if lado1**2 == (lado2**2 + lado3**2):
        print(f'A hipotenusa do triângulo é {lado1} e seus catetos são {lado2} e {lado3}.')
    
    elif lado2**2 == (lado1**2 + lado3**2):
        print(f'A hipotenusa do triângulo é {lado2} e seus catetos são {lado1} e {lado3}.')
    
    elif lado3**2 == (lado1**2 + lado2**2):
        print(f'A hipotenusa do triângulo é {lado3} e seus catetos são {lado1} e {lado2}.')
    
    else:
        print('O triângulo não é retângulo.')


main()
