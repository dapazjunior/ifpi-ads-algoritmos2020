def main():
    n = int(input('Digite um número: '))
    atual = 1
    soma = 0

    while atual <= n:
        termo = (atual * 2 - 1)/atual
        
        soma += termo
        atual += 1
                
    
    print(soma)
        

main()
