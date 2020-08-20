def main():
    dividendo = int(input('Digite o dividendo: '))
    divisor = int(input('Digite o divisor: '))
    
    if divisor == 0:
        print('O divisor não pode ser zero! Refaça a operação')
        main()
    
    else:
        quociente = 0
        
        while dividendo >= divisor:
            dividendo -= divisor
            quociente += 1
        
        resto = dividendo
                
        print(f'Quociente: {quociente}\nResto: {resto}')


main()
