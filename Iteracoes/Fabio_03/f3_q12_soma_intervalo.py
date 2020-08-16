def main():
    n = int(input('Quantos números vai digitar? '))
    soma = 0
    cont = 0
    
    while cont < n:
        num = int(input('Digite um número: '))
        soma += num
        cont += 1
    
    media = soma / n

    print(f'A soma dos números é {soma}.\nA média dos números é {media}')


main()