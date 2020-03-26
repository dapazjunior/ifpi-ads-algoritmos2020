def main():
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))
    num3 = float(input('Digite outro número: '))
    
    soma_1_e_2 = calc_soma_1_e_2(num1, num2)
    
    diferenca_2_e_3 = calc_diferenca_2_e_3(num2, num3)
    
    print (f'A soma entre {num1} e {num2} é {soma_1_e_2}, e a diferença entre {num2} e {num3} é {diferenca_2_e_3}.')


def calc_soma_1_e_2(numero_1, numero_2):
    soma = numero_1 + numero_2
    return soma


def calc_diferenca_2_e_3(numero_2, numero_3):
    diferenca = numero_2 - numero_3
    return diferenca


main()
