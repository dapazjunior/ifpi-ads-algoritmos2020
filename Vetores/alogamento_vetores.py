def main():
    print('> VETORES - Exercício 1\n')
    qtd = int(input('Quantos números serão digitados? '))

    vetor = inserir_dados(qtd)
    calcular_quantidades(vetor)
    
    vetor = substituir_dados(vetor)
    calcular_quantidades(vetor)
    media = calcular_media(vetor)
    
    print(f'> Média após transformação: {media:.2f}')
    

def inserir_dados(qtd):
    vetor = [-1] * qtd
    indice = 0
            
    while indice < len(vetor):
        vetor[indice] = int(input('Valor: '))
        indice += 1

    return vetor


def calcular_quantidades(vetor):
    pares = qtd_pares(vetor)
    impares = qtd_impares(vetor)
    negativos = qtd_negativos(vetor)
    positivos = qtd_positivos(vetor)
    
    print('\n### Quantidades ###\n' \
    + f'> Pares: {pares}\n' \
    + f'> Ímpares: {impares}\n' \
    + f'> Positivos: {positivos}\n' \
    + f'> Negativos: {negativos}\n')


def substituir_dados(vetor):
    indice = 0
    
    for num in vetor:
        if eh_positivo(num):
            vetor[indice] = vetor[indice] * 2
        
        elif num != 0:
            vetor[indice] = vetor[indice] / 2
    
    return vetor


def calcular_media(vetor):
    soma = 0
    
    for num in vetor:
        soma += num
    
    media = soma / len(vetor)
    
    return media


def qtd_pares(vetor):
    num_pares = 0
    
    for num in vetor:
        if eh_par(num):
            num_pares += 1
    
    return num_pares


def qtd_impares(vetor):
    num_impares = 0
    
    for num in vetor:
        if not eh_par(num):
            num_impares += 1
    
    return num_impares


def qtd_positivos(vetor):
    num_positivos = 0
    
    for num in vetor:
        if eh_positivo(num):
            num_positivos += 1
    
    return num_positivos


def qtd_negativos(vetor):
    num_negativos = 0
    
    for num in vetor:
        if not eh_positivo(num) and num != 0:
            num_negativos += 1
    
    return num_negativos


def eh_positivo(num):
    if num > 0:
        return True
    else:
        return False


def eh_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


main()