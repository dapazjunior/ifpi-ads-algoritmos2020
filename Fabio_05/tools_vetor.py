def criar_vetor(n):
    vetor = []
    
    for i in range(n):
        elemento = input(f'Posição [{i}]: ')
        vetor.append(elemento)
    
    return vetor