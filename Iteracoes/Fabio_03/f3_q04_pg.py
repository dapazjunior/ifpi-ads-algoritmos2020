def main():
    termo_a0 = int(input('Digite o valor de A0 da PG: '))
    limite = int(input('Digite o valor limite da PG: '))
    razao = int(input('Digite o valor da razão da PG: '))

    cont = 0
    termo = termo_a0

    if razao == 1:
        print(termo_a0)
    
    else:
        while termo <= limite:
            print(termo)
            cont += 1
            termo = termo_a0 * razao ** cont
            

main()
