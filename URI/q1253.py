def main():
    qtd_teste = int(input())

    for _ in range(qtd_teste):
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        texto = input()
        mudar_posicao = int(input())
        texto_convertido = ''

        for letra in texto:
            if letra in alfabeto:
                pos = alfabeto.find(letra)
                pos -= mudar_posicao

                texto_convertido += alfabeto[pos]

        print (texto_convertido)

main()