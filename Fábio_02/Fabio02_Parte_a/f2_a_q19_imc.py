def main():
    peso = float(input('Digite o peso: '))
    altura = float(input('Digite a altura: '))
    
    imc = calcular_imc(peso, altura)
    
    classificacao = verificar_imc(imc)
    print(f'IMC = {imc:.1f}')
    print(f'Você está com {classificacao}.')
    

def calcular_imc(peso, altura):
    imc = peso / altura**2
    return imc


def verificar_imc(imc):
    if imc < 25.0:
        return 'o peso normal'
    elif imc >= 25.0 and imc < 30.0:
        return 'obesidade'
    else:
        return 'obesidade mórbida'


main()
