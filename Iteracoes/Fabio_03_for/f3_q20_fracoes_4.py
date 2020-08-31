def main():
    n = int(input('Digite um número: '))
    soma = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            termo = - 1/i
        else:
            termo = 1/i
        
        soma += termo
                
    
    print(soma)
        

main()
