def main():
    n = int(input('Digite um número: '))
    soma = 0
    atual = 1

    while atual <= n:
        termo = atual / (n - atual + 1)
        soma += termo
                
        atual += 1
    
    print(soma)
        

main()