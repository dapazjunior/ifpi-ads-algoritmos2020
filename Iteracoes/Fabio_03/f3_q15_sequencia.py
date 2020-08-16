def main():
    n = int(input('Digite um número: '))
    soma = 0
    cont = 1
    lista = []

    while cont <= n:
        soma += cont
        lista.append(soma)
        cont += 1
    
    print (lista)
    

main()