def main():
    num = int(input('Digite um número: '))
    fatorial = num
    produto = num
    
    while num > 1:
        produto = produto * (num - 1)
        num = num - 1
    
    print (f'{fatorial}! = {produto}')
        

main()
