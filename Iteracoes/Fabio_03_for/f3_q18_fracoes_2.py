def main():
    n = int(input('Digite um número: '))
    soma = 0

    for i in range(1, n + 1):
        termo = i/(n - i + 1)
        soma += termo
    
    print(soma)
        

main()