def main():
    num = int(input('Digite um número inteiro na base decimal: '))
    num_bin = 0
    divisoes = 0

    while num != 0:
        num = num - (num // 2) - (num % 2)
        num_bin = num_bin + ((num % 2) * (10 ** divisoes))
        digito = ((num % 2) * (10 ** divisoes))
        divisoes += 1
        print(digito)
        print(num)
    
    print(f'Binário: {num_bin}')


main()
