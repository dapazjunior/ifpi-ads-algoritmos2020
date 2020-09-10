def main():
    tempo = int(input())
    vel = int(input())
    
    rendimento = 12 #km/l
    
    dist = vel * tempo
    
    consumo = dist / rendimento
    
    print(f'{consumo:.3f}')


main()