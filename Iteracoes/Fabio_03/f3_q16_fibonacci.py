def main():
    n = int(input('Digite um número: '))
    lista = [0, 1]
    cont = 2

    if n == 2:
        lista = lista
    else:
        while cont < n:
            lista.append(lista[cont-1] + lista[cont-2])
            cont += 1
    
    print (lista)
    

main()