def main():
    qtd_n = int(input())

    for _ in range(qtd_n):
        n1, n2 = map(float, input().split())
        
        if n2 == 0:
            print('divisao impossivel')
        else:
            div = n1 / n2
            print('{:.1f}'.format(div))

main()