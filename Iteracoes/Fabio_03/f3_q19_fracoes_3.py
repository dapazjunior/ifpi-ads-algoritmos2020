def main():
    n = int(input('Digite um número: '))
    atual = 1
    soma = 0

    while atual <= n:
        if atual % 2 == 0:
            termo = - (n - atual + 1)/atual
        else:
            termo = atual/(n - atual + 1)
        
        soma += termo
        atual += 1
                
    
    print(soma)
        

main()
