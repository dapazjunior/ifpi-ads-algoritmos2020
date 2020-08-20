def main():
    num_1 = int(input('Digite um número: '))
    num_2 = int(input('Digite um número: '))
    
    if num_1 == 0 or num_2 == 0:
        soma = 0
    
    else:
        soma = num_2
        cont_num_1 = 1
        
        while cont_num_1 < num_1:
            soma += num_2
            cont_num_1 += 1
        
    print(soma)


main()
