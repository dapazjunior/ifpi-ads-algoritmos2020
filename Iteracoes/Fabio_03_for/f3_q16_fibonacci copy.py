def main():
    n = int(input('Digite um número: '))
    lista = [0, 1]

    if n == 2:
        lista = lista
    else:
        for i in range(2, n):
            lista.append(lista[i-1] + lista[i-2])
    
    print (lista)
    

main()