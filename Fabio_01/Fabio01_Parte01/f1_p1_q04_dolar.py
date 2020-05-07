def main():
    dolar1 = float(input('Digite um valor em dólar: '))
    dolar2 = float(input('Digite outro valor em dólar: '))

    dolar_total = somar_dolar(dolar1, dolar2)
    real = conversor(dolar_total)

    print(f'O valor é R$ {real:.2f}')


def somar_dolar(dolar1, dolar2):
    dolar_total = dolar1 + dolar2
    return dolar_total


def conversor(dolar_total):
    real = dolar_total * 4.98
    return real


main()
