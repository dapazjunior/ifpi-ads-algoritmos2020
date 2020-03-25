def main():
    numero = int(input('Digite um numero inteiro de 3 algarismos: '))
    
    soma = soma_algs(numero)
    
    print(f'A soma dos algarismos é {soma}.')


def alg_centena(numero):
    centena = numero // 100
    return centena


def alg_dezena(numero):
    dezena = (numero % 100) // 10
    return dezena


def alg_unidade(numero):
    unidade = (numero % 100) % 10
    return unidade

def soma_algs(numero):
    c = alg_centena(numero)
    d = alg_dezena(numero)
    u = alg_unidade(numero)
    
    soma = c + d + u
    
    return soma


main()
