def main():
    qtd = 0
    somatorio = 0
    num = int(input('Digite um número: '))
    
    while num >= 0:
        somatorio +=  num
        qtd += 1
        
        num = int(input('Digite um número: '))
    
    media = somatorio/qtd
    print(media)

main()