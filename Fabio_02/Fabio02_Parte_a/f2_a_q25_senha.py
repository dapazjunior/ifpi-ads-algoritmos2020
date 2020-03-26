def main():
    senha = int(input('Digite a senha:\n     '))
    
    if senha == 1234:
        print('ACESSO LIBERADO!')
    
    else:
        print('ACESSO NEGADO!')
        main()


main()
