def main():
    qtd = int(input())

    for _ in range(qtd):
        n1, n2, n3 = map(float, input().split())
        media_ponderada = (n1*2 + n2*3 + n3*5) / 10
        print('{:.1f}'.format(media_ponderada))

main()