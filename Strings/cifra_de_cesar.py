def rotate_word():
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    texto = input('Qual o texto que você deseja rotacionar?\n')
    texto = texto.upper()
    
    mudar_posicao = int(input('Qual o fator para rotacionar o texto?\n'))
    texto_convertido = ''

    for letra in texto:
        if letra in alfabeto:
            pos = alfabeto.find(letra)
            pos = pos + mudar_posicao

            texto_convertido = texto_convertido + alfabeto[pos]

    print ('Texto rotacionado: ' + texto_convertido)


rotate_word()