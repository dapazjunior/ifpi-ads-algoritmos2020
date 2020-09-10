def main():
    frase = input('Digite a frase:\n>>> ')
    palavra = input('Digite a palavra que seja procurar:\n>>> ')
    
    if contem(palavra, frase) == True:
        print('Sim. Palavra encontrada na frase!')
    
    else:
        print('Não. A frase não contem a palavra!')


def contem(word, frase):
    indice_frase = 0
    limite = len(frase) - len(word) + 1
        
    while indice_frase < len(frase):
        if (frase[indice_frase] == word[0]) and (indice_frase < limite):
            if verificar_substring(word, frase, indice_frase) == True:
                return True
                
        indice_frase += 1
        
    return False

                    
def verificar_substring(word, frase, indice_frase):
    letras_iguais = 0
    indice_word = 0
        
    while indice_word < len(word):
        if verificar_caractere(word[indice_word], frase[indice_frase]):
            letras_iguais += 1
            
        indice_word += 1
        indice_frase += 1
    
    if letras_iguais == len(word):
        return True
    else:
        return False


def verificar_caractere(char1, char2):
    if char1 == char2:
        return True
    else:
        return False


main()
