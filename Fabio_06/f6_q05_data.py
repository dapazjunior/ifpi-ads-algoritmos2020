def main():
    data = input('Digite a data (DD/MM/AAAA):\n>> ')
    
    nova_data = mudar_formato_data(data)
    
    print(nova_data)


def mudar_formato_data(data):
    dia = data[0:2]
    mes = selecionar_mes(int(data[3:5]))
    ano = data[6:10]
    
    data_transformada = f'{dia} de {mes} de {ano}'
    
    return data_transformada


def selecionar_mes(num):
    if num == 1:
        mes = 'janeiro'
    elif num == 2:
        mes = 'fevereiro'
    elif num == 3:
        mes = 'março'
    elif num == 4:
        mes = 'abril'
    elif num == 5:
        mes = 'maio'
    elif num == 6:
        mes = 'junho'
    elif num == 7:
        mes = 'julho'
    elif num == 8:
        mes = 'agosto'
    elif num == 9:
        mes = 'setembro'
    elif num == 10:
        mes = 'outubro'
    elif num == 11:
        mes = 'novembro'
    elif num == 12:
        mes = 'dezembro'
    
    return mes


main()
