def main():
    n = int(input('Quantos números vai digitar? '))
    maior = 0
    
    for _ in range(1, n + 1):
        num = int(input('Digite um número: '))
        if num > maior:
            maior = num
    
    
    print(f'O maior número é {maior}.')


main()
