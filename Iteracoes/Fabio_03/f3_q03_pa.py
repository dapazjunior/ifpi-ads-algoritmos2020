def main():
    termo_a0 = int(input('Digite o valor de A0 da PA: '))
    limite = int(input('Digite o valor limite da PA: '))
       
    razao = int(input('Digite o valor da razão da PA: '))
    
    termo = termo_a0

    if razao == 0:
            print(termo_a0)
            
    else:
        while termo <= limite:
            print(termo)
            termo += razao                             


main()
