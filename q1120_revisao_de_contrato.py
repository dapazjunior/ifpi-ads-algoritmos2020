def main():
    while True:
        tecla_errada, numero = input().split(' ')
        
        if tecla_errada == '0' and numero == '0':
            break
        
        revisar_contrato(tecla_errada, numero)
    
    

def revisar_contrato(tc, num):
    valor = ''
    
    for c in num:
        if c == tc:
            pass
        else:
            valor += c
        
    if valor == '':
        valor = 0
    else:
        valor = int(valor)
        
    print(valor)


main()
