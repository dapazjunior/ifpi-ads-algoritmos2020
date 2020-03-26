def main ():
    numero = float(input('Digite um número: '))
    
    num_arredondado = arredondar(numero)
    
    print(f'O arredondamento do número {numero} é {num_arredondado}.')
    
    
def arredondar(num):
    fracao = num - int(num)
    
    if fracao >= 0.5:
        num = int(num) + 1
        return num
    elif fracao < 0.5:
        num = int(num)
        return num


main()
