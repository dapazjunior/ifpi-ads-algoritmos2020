def main():
    n = int(input('Digite um número: '))
    atual = 1
    soma = 0

    while atual <= n:
        if atual % 2 == 0:
            termo = - 1/atual
        else:
            termo = 1/atual
        
        soma += termo
        atual += 1
                
    
    print(soma)
        

main()
