def rotate_word():
    texto = input('Qual o texto que você deseja rotacionar?\n')
    rotacao = int(input('Qual o fator para rotacionar o texto?\n'))
    
    texto_encriptado = ''
    
    for caractere in texto:
        if eh_letra(caractere):
            novo_caractere = rotacionar_caractere(caractere, rotacao)
        else:
            novo_caractere = caractere
        
        texto_encriptado += novo_caractere 
            
    
    print ('Texto encriptado >>> ' + texto_encriptado)
    

def rotacionar_caractere(c, rot):
    indice_c_encrip = ord(c) + rot
       
    if (eh_maiuscula(c) and indice_c_encrip > 90) or (eh_minuscula(c) and indice_c_encrip > 122):
        indice_c_encrip -= 26
    
    c_encriptado = chr(indice_c_encrip) 
    return c_encriptado


def eh_maiuscula(c):
    return (ord('A') <= ord(c) <= ord('Z'))


def eh_minuscula(c):
    return (ord('a') <= ord(c) <= ord('z'))


def eh_letra(c):
    return eh_minuscula(c) or eh_maiuscula(c)


rotate_word()