def main():
    tipo = input('Escolha o combustível:\nA - Álcool\nG - Gasolina\n>>> ').lower()
    
    tipo = verificar_tipo(tipo)
    
    litros = float(input(f'\nQuantos litros de {tipo} você deseja colocar?\n>>> '))
    
    valor = calcular_preco(tipo, litros)
    
    print(f'\n>>>>>> RECIBO <<<<<<\nCombustível: {tipo}\nLitros: {litros}\nValor: R$ {valor:.2f}\n\n-=-=-=-=-=-=-=-=-=-=')
    

def verificar_tipo(tipo):
    if tipo == 'a':
        return 'Álcool'
    elif tipo == 'g':
        return 'Gasolina'


def calcular_preco(tipo, litros):
    if tipo == 'Álcool':
        if litros <= 20:
            preco = litros * 1.9 * 0.97
            return preco
        else:
            preco = litros * 1.9 * 0.95
            return preco
    elif tipo == 'Gasolina':
        if litros <= 20:
            preco = litros * 2.5 * 0.96
            return preco
        else:
            preco = litros * 2.5 * 0.94
            return preco


main()
