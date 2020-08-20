def main():
    while True:
        produto = input('\nNome do produto: ').upper()
        if produto == 'FIM':
            break
        
        preco_unit = float(input('Preço do produto: R$ '))
        qtde = int(input('Quantidade: '))
        desconto = verificar_desconto(qtde)
        
        preco_total = preco_unit * qtde * (1 - desconto)
        
        print(f'\nPRODUTO\n>> {produto}\nVALOR:\n>> R$ {preco_total:.2f}')

       
def verificar_desconto(qtd):
    if qtd < 10:
        desc = 0
        return desc
    elif qtd < 20:
        desc = 0.1
        return desc
    elif qtd < 50:
        desc = 0.2
        return desc
    else:
        desc = 0.25
        return desc


main()
