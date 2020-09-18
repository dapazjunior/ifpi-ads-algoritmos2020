def main():
    arquivo = open('words.txt')
    
    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) > 20:
            print(palavra)
    
    
    arquivo.close()


main()