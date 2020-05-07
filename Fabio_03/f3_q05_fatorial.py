def main():
    num = int(input('Digite um número: '))
    fatorial = num
    produto = num
    
    for _ in range(1, num):
        produto = produto * (num - 1)
        num = num - 1
    
    print (f'{fatorial}! = {produto}')
        

main()
