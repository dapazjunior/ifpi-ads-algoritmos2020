def main():
    a = int(input('Digite o valor de "a": '))
    b = int(input('Digite o valor de "b": '))
    c = int(input('Digite o valor de "c": '))

    delta = calcular_delta(a, b, c)
    raizes(a, b, delta)


def calcular_delta(a, b, c):
    d = b**2 - 4 * a * c
    return d

def raizes(a, b, delta):
    if delta > 0:
        x1 = (-b + delta**(1/2))/(2 * a)
        x2 = (-b - delta**(1/2))/(2 * a)
        print(f'As raízes da função são {x1} e {x2}.')
    
    elif delta == 0:
        x = -b/(2 * a)
        print(f'A raiz da função é {x}.')
    
    else:
        print('A função não possui raízes reais.')


main()
