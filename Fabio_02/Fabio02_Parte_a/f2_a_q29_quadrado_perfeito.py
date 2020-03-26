from math import sqrt
def main():
    num = int(input('Digite um número de 4 dígitos: '))
    
    verificar_quadrado_perfeito(num)


def verificar_quadrado_perfeito(num):
    parte1 = num // 100
    parte2 = num % 100
    
    soma = parte1 + parte2
    
    raiz = sqrt(num)
    
    if soma == raiz:
        print('O número é quadrado perfeito.')
    else:
        print('O número não é quadrado perfeito.')


main()
