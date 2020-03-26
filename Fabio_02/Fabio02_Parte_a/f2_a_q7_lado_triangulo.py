def main():
    lado1 = int(input('Digite a medida do primeiro lado: '))
    lado2 = int(input('Digite a medida do segundo lado: '))
    lado3 = int(input('Digite a medida do terceiro lado: '))
    
    eh_triangulo = verificar_se_triangulo(lado1, lado2, lado3)
    classificacao = classificar_triangulo(lado1, lado2, lado3)
    
    if eh_triangulo == True:
        print (f'O triangulo é {classificacao}')
    else:
        print ('Os segmentos não formam um triângulo.')


def verificar_se_triangulo(lado1, lado2, lado3):
    if (lado1 < (lado2 + lado3)) and (lado2 < (lado1 + lado3)) and (lado3 < (lado1 + lado2)):
        return True
    else:
        return False


def classificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return 'Equilátero'
    elif (lado1 == lado2 != lado3) or (lado2 == lado3 != lado1) or (lado1 == lado3 != lado2):
        return 'Isósceles'
    else:
        return 'Escaleno'


main()
