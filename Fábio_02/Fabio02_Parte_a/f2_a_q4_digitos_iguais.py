def main():
    num1 = int(input('Digite um número de dois algarismos: '))
    
    igual = verificar_se_igual(num1)
    
    if igual == True:
        print('Os algarismos são igauis.')
    else:
        print('Os algarismos são diferentes.')
    


def verificar_se_igual(num1):
    dez = num1 // 10
    unid = num1 % 10
    
    if dez == unid:
        return True
    else:
        return False


main()
