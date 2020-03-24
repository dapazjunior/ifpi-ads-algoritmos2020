def main():
    qual_carne = input('Qual carne você deseja?\nDigite:\nF - Filé\nA - Alcatra\nP - Picanha\n>>> ').lower()
    
    carne = verificar_carne(qual_carne)
    
    quantos_kg = float(input(f'\nQuantos kg de {carne} você deseja?\n>>> '))
    
    valor_parcial = calc_valor_parcial(qual_carne, quantos_kg)
        
    forma_pagamento = input('\nDeseja pagar com o Cartão Tabajara?\nS - Sim\nN- Não\n>>> ').lower()
    
    desconto = calcular_desconto(valor_parcial, forma_pagamento)
    
    valor_final = valor_parcial - desconto
    
    print(f'\n>>>>>> CUPOM FISCAL <<<<<<\n{carne} ---- {quantos_kg}kg\nDesconto ----- - R${desconto:.2f}')
    print(f'Total: R$ {valor_final:.2f}\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=\nb') 


def verificar_carne(qual_carne):
    if qual_carne == 'f':
        return 'filé'
    elif qual_carne == 'a':
        return 'alcatra'
    elif qual_carne == 'p':
        return 'picanha'


def calc_valor_parcial(qual_carne, quantos_kg):
    if qual_carne == 'f':
        valor_file = calcular_file(quantos_kg)
        return valor_file
    elif qual_carne == 'a':
        valor_alcatra = calcular_alcatra(quantos_kg)
        return valor_alcatra
    elif qual_carne == 'p':
        valor_picanha = calcular_picanha(quantos_kg)
        return valor_picanha

    
def calcular_file(quantos_kg):
    if quantos_kg <= 5:
        preco = quantos_kg * 4.9
        return preco
    else:
        preco = quantos_kg * 5.8
        return preco

def calcular_alcatra(quantos_kg):
    if quantos_kg <= 5:
        preco = quantos_kg * 5.9
        return preco
    else:
        preco = quantos_kg * 6.8
        return preco


def calcular_picanha(quantos_kg):
    if quantos_kg <= 5:
        preco = quantos_kg * 6.9
        return preco
    else:
        preco = quantos_kg * 7.8
        return preco


def calcular_desconto(valor_parcial, forma_pagamento):
    if forma_pagamento == 's':
        desconto = valor_parcial * 0.05
        return desconto
    else:
        desconto = 0
        return desconto  


main()
