def criar_vetor(n):
    vetor = []
    
    for i in range(n):
        elemento = input(f'Posição [{i}]: ')
        vetor.append(elemento)
    
    return vetor


def criar_vetor_num(n):
    vetor = []
    
    for i in range(n):
        elemento = int(input(f'Posição [{i}]: '))
        vetor.append(elemento)
    
    return vetor