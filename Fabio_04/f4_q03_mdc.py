def main():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))

    mdc = num1
    if num2 < num1:
        mdc = num2
    
    while not(num1 % mdc == 0 and num2 % mdc == 0):
        mdc -= 1
    
    print (f'O MDC de {num1} e {num2} é {mdc}')


main()
