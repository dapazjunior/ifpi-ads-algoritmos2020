def main():
    n = int(input('Quantos números vai digitar? '))
    soma = 0
    
    for _ in range(n):
        num = int(input('Digite um número: '))
        soma += num
    
    media = soma / n

    print(f'A soma dos números é {soma}.\nA média dos números é {media}')


main()
