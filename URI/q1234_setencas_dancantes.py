def principal():
    while True:
        try:
            texto = input()
    
            texto = dancar(texto)
            print(texto)
        except EOFError:
            break


def dancar(txt):
    novo_txt = ''
    letras = 1
    
    for c in txt:
        if c == ' ':
            novo_txt += c
        else:
            if letras % 2 != 0:
                c = c.upper()
            else:
                c = c.lower()
            
            novo_txt += c
        
            letras += 1
    
    return novo_txt


principal()