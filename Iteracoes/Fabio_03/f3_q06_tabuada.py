def main():
    fator_1 = 1
    fator_2 = 1
    
    while fator_2 <= 10:
        print(f'Tabuada de {fator_2}')
        
        while fator_1 <= 10:
            produto = fator_1 * fator_2
            print(f'{fator_1} x {fator_2} = {produto}')
            fator_1 += 1
        
        print()
        fator_2 += 1
        fator_1 = 1


main()