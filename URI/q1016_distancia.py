def main():
    v1 = 1 #km/min
    v2 = 1.5 #km/min
    
    v_relativa = v2 - v1
    
    dist = int(input())
    
    tempo = dist / v_relativa
    
    print(f'{tempo:.0f} minutos')


main()