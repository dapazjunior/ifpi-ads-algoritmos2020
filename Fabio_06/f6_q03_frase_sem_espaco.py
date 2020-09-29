def main():
    frase = input('Digite a frase:\n>> ')
    
    print_sem_espaco(frase)


def print_sem_espaco(string):
    nova_string = ''
    for c in string:
        
        if c != ' ':
            nova_string += c
        
    print(nova_string)        


main()