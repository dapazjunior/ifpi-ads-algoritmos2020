import math

def main():
    n = int(input('Quantos números vai digitar? '))
    maior = -math.inf
    
    for _ in range(n):
        num = int(input('Digite um número: '))
        if num > maior:
            maior = num
    
    print(f'O maior número é {maior}.')


main()
