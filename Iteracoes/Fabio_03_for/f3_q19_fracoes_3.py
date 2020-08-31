def main():
    n = int(input('Digite um número: '))
    soma = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            termo = - (n - i + 1)/i
        else:
            termo = i/(n - i + 1)
        
        soma += termo
                
    
    print(soma)
        

main()
