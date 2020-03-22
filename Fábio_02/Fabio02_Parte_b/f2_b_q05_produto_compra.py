def main():
    preco1 = float(input('Digite o preço do primeiro produto: '))
    preco2 = float(input('Digite o preço do segundo produto: '))
    preco3 = float(input('Digite o preço do terceiro produto: '))
    
    produto_compra = comparar_precos(preco1, preco2, preco3)
    
    print(f'O {produto_compra} produto será comprado.')


def comparar_precos(preco1, preco2, preco3):
    if preco1 < preco2 and preco1 < preco3:
        return 'primeiro'
    elif preco2 < preco1 and preco2 < preco3:
        return 'segundo'
    elif preco3 < preco1 and preco3 < preco2:
        return 'terceiro'
    elif preco1 == preco2 and preco1 < preco3:
        return 'primeiro ou segundo'
    elif preco1 == preco3 and preco1 < preco2:
        return 'primeiro ou terceiro'
    elif preco2 == preco3 and preco2 < preco1:
        return 'segundo ou terceiro'
    else:
        return 'primeiro, segundo ou terceiro'


main()
