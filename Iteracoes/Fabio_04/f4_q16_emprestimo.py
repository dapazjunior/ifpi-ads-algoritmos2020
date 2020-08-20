def main():
    emprestimo = float(input('Valor do empréstimo: '))
    pag_diario = float(input('Pagamento diário (dias úteis): '))
    dia_pag = int(input('Qual o dia do início do pagamento?\nDom - 1\nSeg - 2\nTer - 3\nQua - 4\nQui - 5\nSex - 6\nSáb - 7\n>>> '))

    dias_uteis = 0
    
    while emprestimo > 0:
        if verificar_se_util(dia_pag):
            emprestimo -= pag_diario
            dias_uteis += 1
        
        emprestimo += emprestimo * 0.0085
        dia_pag += 1

        
    print(f'São necessários {dias_uteis} dias úteis para finalizar o pagamento.')

def verificar_se_util(dia):
    if (dia % 7) <= 5:
        return True
    else:
        return False        


main()
