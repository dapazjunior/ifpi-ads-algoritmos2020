def main():
    for i in range(1,11):
        print(f'Tabuada do {i}')
        for c in range (1,11):
            produto = c * i
            print(f'{i} x {c} = {produto}')
        print('\n')


main()
