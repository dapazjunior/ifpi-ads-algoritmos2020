def main():
    angulo = int(input('Digite um ângulo em graus: '))
    
    quadrante = verificar_quadrante(angulo)
    
    if angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270:
        print(f'O ângulo {angulo}° está no eixo de intercessão dos quadrantes.')
    else:
        print(f'O ângulo {angulo}° está no {quadrante} quadrante.')


def verificar_quadrante(angulo):
    if angulo % 360 > 0 and angulo % 360 < 90:
        return 'primeiro'
    elif angulo % 360 > 90 and angulo % 360 < 180:
        return 'segundo'
    elif angulo % 360 > 180 and angulo % 360 < 270:
        return 'terceiro'
    elif angulo % 360 > 270 and angulo % 360 < 360:
        return 'quarto'


main()
