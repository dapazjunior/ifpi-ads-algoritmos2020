def main():
    morango = float(input('Quantos kg de morango?\n>>> '))
    maca = float(input('Quantos kg de maçã?\n>>> '))
    
    valor_morango = calcular_morango(morango)
    valor_maca = calcular_maca(maca)
    
    desconto = calcular_desconto(morango, maca, valor_morango, valor_maca)
    
    valor_final = (valor_maca + valor_morango) * (1 - desconto)
    
    print(f'\n>>>>>> RECIBO <<<<<<\nMorango: {morango:.1f} kg')
    print(f'Maça: {maca:.1f} kg\n\nTotal: R$ {valor_final:.2f}\n\n-=-=-=-=-=-=-=-=-=-=')

def calcular_morango(morango):
    if morango <= 5:
        preco = morango * 2.5
        return preco
    else:
        preco = morango * 2.2
        return preco

def calcular_maca(maca):
    if maca <= 5:
        preco = maca * 1.8
        return preco
    else:
        preco = maca * 1.5
        return preco

def calcular_desconto(morango, maca, valor_morango, valor_maca):
    peso_total = morango + maca
    valor_total = valor_morango + valor_maca
    
    if peso_total > 8 or valor_total > 25:
        desconto = 0.1
        return desconto
    else:
        desconto = 0
        return desconto


main()
