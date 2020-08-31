def main():
    n = int(input('Digite um número: '))
    soma = n
    
    for _ in range(1, n + 1):
        soma += (n - 1)
        n -= 1
    
    print(soma)

main()
