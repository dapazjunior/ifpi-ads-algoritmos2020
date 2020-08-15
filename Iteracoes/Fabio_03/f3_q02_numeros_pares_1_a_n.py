def main():
    contador = 1
    n = int(input('Digite um número: '))

    while contador <= n:
        if contador % 2 == 0:
            print(contador)
        
        contador += 1


main()