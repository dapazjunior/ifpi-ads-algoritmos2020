from tools_vetor import criar_vetor_num

def main():
    qtd = int(input('Quantos elementos terão os vetores? '))
    vetor_a = criar_vetor_num(qtd)

    vetor_b = []

    for num in vetor_a:
        if eh_par(num):
            vetor_b.append(0)
        
        else:
            vetor_b.append(1)
    
    print(f'A: {vetor_a}')
    print(f'B: {vetor_b}')


def eh_par(num):
    if num % 2 == 0:
        return True
    
    return False

main()
