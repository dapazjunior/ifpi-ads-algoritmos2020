def main():
    qtd = int(input())
    
    for _ in range(qtd):
        num = input()
        
        qtd_leds = verificar_leds(num)
        
        print(f'{qtd_leds} leds')


def verificar_leds(numero):
    num_leds = 0
    
    for caractere in numero:
        leds = qtos_leds(caractere)
        num_leds += leds
    
    return num_leds


def qtos_leds(c):
    if c == '1':
        leds = 2
    elif c == '7':
        leds = 3
    elif c == '4':
        leds = 4
    elif c == '2' or c == '3' or c =='5':
        leds = 5
    elif c == '0' or c == '6' or c == '9':
        leds = 6
    else:
        leds = 7
    
    return leds

main()