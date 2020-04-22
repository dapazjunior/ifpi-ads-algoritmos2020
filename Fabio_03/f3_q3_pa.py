def main():
    termo_a0 = int(input('Digite o valor de A0 da PA: '))
    limite = int(input('Digite o valor limite da PA: '))
    razao = int(input('Digite o valor da razão da PA: '))

    cont = 0

    if razao == 0:
            print(termo_a0)
    else:
        for _ in range(0, limite + 1):
            termo = termo_a0 + razao * cont
            cont += 1

            if termo <= limite:
                print(termo)


main()
