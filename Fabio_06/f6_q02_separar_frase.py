def main():
    frase = input('Digite a frase:\n>> ')
    
    print_palavras(frase)


def print_palavras(string):
    palavra = ''
    for c in string:
        
        if c == ' ':
            print(palavra)
            palavra = ''
        
        else:
            palavra += c
        
    print(palavra)        


main()