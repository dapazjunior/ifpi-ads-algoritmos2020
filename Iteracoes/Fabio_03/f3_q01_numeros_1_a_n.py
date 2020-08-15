def main():
    contador = 0
    qtd_n = int(input('Digite um número: ')) # O valor digitado será o último número da sequência
    
    while contador < qtd_n:
        num = 1 + contador
        contador += 1
        print(num)
    

main()