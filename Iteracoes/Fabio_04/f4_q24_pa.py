def main():
    razao = int(input('Digite a razão da sua PG: '))
    termo = int(input('Digite o primeiro termo da PG: '))
    n = int(input('Digite a quantidade de termos: '))
    pa = [termo]
    
    while n > 1:
        termo = termo + razao
        pa.append(termo)
        n -= 1
    
    print(f'PA = {pa}')


main()
