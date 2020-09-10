def main():
    while True:
        try:
            num_palavras, max_linhas, max_caracteres = input().split(' ')
            
            num_palavras = int(num_palavras)
            max_linhas = int(max_linhas)
            max_caracteres = int(max_caracteres)
            
            conto = input()
            
            if num_palavras == '0':
                break
            
            num_caracteres = len(conto)
            
            num_linhas = calc_linhas(num_caracteres, max_caracteres)
            num_paginas = calc_paginas(num_linhas, max_linhas)
            
            print(num_paginas)
        
        except EOFError:
            break
        

def calc_linhas(num_char, max_char):
    linhas = num_char // max_char
    if num_char % max_char != 0:
        linhas += 1
    
    return linhas


def calc_paginas(num_lines, max_lines):
    pags = num_lines // max_lines
    if num_lines % max_lines != 0:
        pags += 1
    
    return pags

    
main()