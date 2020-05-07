def main():
    ang1 = int(input('Digite o primeiro ângulo: '))
    ang2 = int(input('Digite o segundo ângulo: '))
    ang3 = int(input('Digite o terceiro ângulo: '))
    
    eh_triangulo = verificar_se_triangulo(ang1, ang2, ang3)
    classificacao = classificar_triangulo(ang1, ang2, ang3)
    
    if eh_triangulo == True:
        print (f'O triangulo é {classificacao}')
    else:
        print ('Os ângulos não formam um triângulo.')


def verificar_se_triangulo(ang1, ang2, ang3):
    if (ang1 + ang2 + ang3 == 180) and (ang1 > 0 and ang2 > 0 and ang3 > 0):
        return True
    else:
        return False


def classificar_triangulo(ang1, ang2, ang3):
    if ang1 < 90 and ang2 < 90 and ang3 < 90:
        return 'Acutângulo'
    elif ang1 == 90 or ang2 == 90 or ang3 == 90:
        return 'Retângulo'
    else:
        return 'Obtusângulo'


main()
