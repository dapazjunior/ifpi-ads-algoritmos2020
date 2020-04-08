def main():
    dias = int(input())
    a = dias // 365
    m = (dias % 365) // 30
    d = (dias % 365) % 30

    print('{} ano(s)'.format(a))
    print('{} mes(es)'.format(m))
    print('{} dia(s)'.format(d))


main()
