def main():
    divisores = []
    
    while True:
        try:
            num = int(input('Digite um número: '))
            for i in range(1, num + 1):
                if num % i == 0:
                    divisores.append(i)
            
            print(f'Os divisores de {num} são: {divisores}')
        except num != 0:
            break

main()
