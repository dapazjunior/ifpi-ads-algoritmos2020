def main():
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    
    calcular(num1, num2)


def calcular(num1, num2):
    resto = num1 % num2
    soma = num1 + num2
    
    if resto == 1:
        valor = resto + soma
        print(f'O valor é {valor}.')
    elif resto == 2:
        par_ou_impar1 = verificar_se_par(num1)
        par_ou_impar2 = verificar_se_par(num2)
        print (f'{num1} é {par_ou_impar1} e ', end = '')
        print (f'{num2} é {par_ou_impar2}')
    elif resto == 3:
        valor = soma * num1
        print(f'O valor é {valor}.')
    elif resto == 4:
        valor = soma % num2
        if valor != 0:
            print(f'O valor é {valor}.')
    else:
        valor1 = num1**2
        valor2 = num2**2
        print(f'Os valores são {valor1} e {valor2}.')
        

def verificar_se_par(num):
    if (num % 2 == 0):
        return 'par'
    else:
        return 'ímpar'


main()
