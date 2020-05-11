def main():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))

    mmc = num1
    if num2 > num1:
        mmc = num2
    
    while not(mmc % num1 == 0 and mmc % num2 == 0):
        mmc += 1
    
    print (f'O MMC de {num1} e {num2} é {mmc}')


main()
