def main():
    x1, y1 = input().split(' ')
    x2, y2 = input().split(' ')
    
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    
    dist = calc_dist_2_pontos(x1, x2, y1, y2)
    print(f'{dist:.4f}')


def calc_dist_2_pontos(a, b, c, d):
    p1 = (a - b) ** 2
    p2 = (c - d) ** 2
    
    distancia = (p1  + p2) ** (1/2)
    return distancia


main()