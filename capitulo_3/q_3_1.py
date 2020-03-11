def main():
    palavra = input('Digite a palavra: ')
    escrever = right_justify (palavra)
    print(escrever)


def right_justify (s):
    tamanho = len(s)
    espaco = 70 - tamanho
    escrever = (espaco*' ' + s)
    return escrever


main()