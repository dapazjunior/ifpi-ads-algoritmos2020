def rotate_word():
    texto = input('Qual o texto que você deseja rotacionar?\n')
    
    rotacao = int(input('Qual o fator para rotacionar o texto?\n'))
    texto_convertido = ''

    for letra in texto:
        if (97 <= (ord(letra) + rotacao) <= 122) or ((ord(letra) + rotacao) <= 90):
            posicao = ord(letra) + rotacao
        elif ((ord(letra) + rotacao) >= 122) or ((ord(letra) + rotacao) >= 90):
            posicao = ord(letra) + rotacao - 26

        texto_convertido = texto_convertido + chr(posicao)

    print ('Texto rotacionado >>>' + texto_convertido)


rotate_word()