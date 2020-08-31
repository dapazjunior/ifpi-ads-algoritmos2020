def main():
    n = int(input('Digite um número: '))
    soma = 0
    lista = []

    for i in range(1, n + 1):
        soma += i
        lista.append(soma)
    
    print (lista)
    

main()
