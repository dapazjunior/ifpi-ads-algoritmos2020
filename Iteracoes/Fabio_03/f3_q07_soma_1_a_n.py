def main():
    n = int(input('Digite um número: '))
    soma = n
    
    while n > 0:
        soma += (n - 1)
        n -= 1
    
    print(soma)

main()
