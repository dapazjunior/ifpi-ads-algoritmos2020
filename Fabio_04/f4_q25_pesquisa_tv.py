def main():    
    assist_2 = 0
    assist_4 = 0
    assist_5 = 0
    assist_7 = 0
    assist_10 = 0
    espectadores = 0
    canal = -1
    
    while canal != 0:
        canal = int(input('Qual o canal sendo assistido? '))
        if canal == 0:
            break
        
        pessoas = int(input('Quantas pessoas estão assistindo? '))
        
        if canal == 2:
            assist_2 += pessoas
        elif canal == 4:
            assist_4 += pessoas
        elif canal == 5:
            assist_5 += pessoas
        elif canal == 7:
            assist_7 += pessoas
        else:
            assist_10 += pessoas
            
        espectadores += pessoas
    
    audiencia_2 = assist_2 / espectadores * 100
    audiencia_4 = assist_4 / espectadores * 100
    audiencia_5 = assist_5 / espectadores * 100
    audiencia_7 = assist_7 / espectadores * 100
    audiencia_10 = assist_10 / espectadores * 100
    
    print('> > > RESULTADO < < <')
    print(f'Audiência 2: {audiencia_2:.1f}%')
    print(f'Audiência 4: {audiencia_4:.1f}%')
    print(f'Audiência 5: {audiencia_5:.1f}%')
    print(f'Audiência 7: {audiencia_7:.1f}%')
    print(f'Audiência 10: {audiencia_10:.1f}%')


main()
