from tools_vetor import criar_vetor

def main():
    qtd = int(input('Quantos elementos? '))

    vetor = criar_vetor(qtd)
    
    if tem_iguais(vetor):
        print('Existem elementos iguais!')
    else:
        print('Não existem elementos iguais!')


def tem_iguais(vetor):
    
    for i in range(len(vetor)):
        pos = i + 1
        
        while pos < len(vetor):
            if vetor[i] == vetor[pos]:
                return True
            
            pos += 1
    
    return False


main()