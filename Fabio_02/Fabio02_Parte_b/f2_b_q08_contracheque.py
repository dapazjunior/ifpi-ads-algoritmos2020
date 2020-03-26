def main():
    valor_hora = float(input('Digite o valor recebido por hora trabalhada:\n>>R$ '))
    horas_trab = int(input('Digite a quantidade de horas trabalhadas: \n>> '))
    
    salario_bruto = horas_trab * valor_hora
    
    irpf = calcular_irpf(salario_bruto)
    sindicato = calcular_sindicato(salario_bruto)
    inss = calcular_inss(salario_bruto)
    fgts = calcular_fgts(salario_bruto)
    
    salario_liquido = calcular_salario(salario_bruto, irpf, sindicato, inss)
    
    print(f'>>>>>>>>>> CONTRACHEQUE <<<<<<<<<<\n\nSalário Bruto: R$ {salario_bruto:.2f}\n(-)Imposto de Renda: R$ {irpf:.2f}' )
    print(f'(-)INSS R$ {inss:.2f}\n(-)Sindicato: {sindicato:.2f}\nFGTS: R$ {fgts:.2f}\nSalário Líquido: R${salario_liquido:.2f}\n')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

def calcular_irpf(salario_bruto):
    if salario_bruto > 0 and salario_bruto <= 900:
        irpf = 0
        return irpf
    elif salario_bruto <= 1500:
        irpf = salario_bruto * 0.05
        return irpf
    elif salario_bruto <= 2500:
        irpf = salario_bruto * 0.10
        return irpf
    else:
        irpf = salario_bruto * 0.20
        return irpf


def calcular_sindicato(salario_bruto):
    sindicato = salario_bruto * 0.03
    return sindicato


def calcular_inss(salario_bruto):
    inss = salario_bruto * 0.1
    return inss


def calcular_fgts(salario_bruto):
    fgts = salario_bruto * 0.11
    return fgts


def calcular_salario(salario_bruto, irpf, sindicato, inss):
    salario_liquido = salario_bruto - irpf - sindicato - inss
    return salario_liquido


main()
