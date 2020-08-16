import math

def main():
    n = int(input('Quantos números vai digitar? '))
    cont = 0
    maior = -math.inf
    
    while cont < n:
        num = int(input('Digite um número: '))
        if num > maior:
            maior = num
        
        cont += 1
    
    print(f'O maior número é {maior}')


main()
