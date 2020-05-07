def main():
    soma = 0
    denominador = 1
    lista = []

    for i in range(1, 100, 2):
        termo = i / denominador
        denominador += 1
        soma += termo
        lista.append(termo)
    
    print(lista)
    print(soma)


main()
