def main():
    inv_mensal = float(input('Investimento mensal:\n>>> R$ '))
    taxa_juros = float(input('Taxa de juros mensal (% mensal)\n>>> '))
    capital_acumulado = 0
    mes = 0
    
    while True:
        capital_acumulado = (capital_acumulado) * (1 + taxa_juros / 100) + inv_mensal
        mes += 1

        if mes == 12:
            print(f'Capital acumulado até agora: R$ {capital_acumulado:.2f}')
            verificar = input('Deseja processar mais um ano (S/N)?\n>>> ').lower()
            
            if verificar == 's':
                mes = 0
            else:
                break
    
    print(f'Capital acumulado final: R$ {capital_acumulado:.2f}')                           
    

main()