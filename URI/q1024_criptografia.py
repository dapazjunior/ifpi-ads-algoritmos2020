def main():
    num = int(input())
    
    for i in range(num):
        strg_criptografar = input()
        
        nova_string = criptografar(strg_criptografar)
        print(nova_string)


def criptografar(strg):
    # Passo 1: Avançar letras 3 casas em ASCII
    nova_str = letras_3_casas(strg)
    
    # Passo 2: Inverter string
    nova_str = inverter_str(nova_str)
    
    # Passo 3: Voltar caracteres 1 casa em ASCII
    nova_str = voltar_1_casa(nova_str)
    
    return nova_str
    

def letras_3_casas(strg):
    str_nova = ''
    
    for c in strg:
        if eh_letra(c):
            novo_car = chr(ord(c) + 3)
        else:
            novo_car = c
        
        str_nova += novo_car
    
    return str_nova


def inverter_str(strg):
    str_nova = ''  
    num_caractere = len(strg)
    
    while num_caractere > 0:
        car_invertido = strg[num_caractere - 1]
        str_nova += car_invertido
        
        num_caractere -= 1
    
    return str_nova


def voltar_1_casa(strg):
    metade_1, metade_2 = dividir_str_em_2(strg)
    
    str_nova = metade_1
    
    for c in metade_2:
        novo_car = chr(ord(c) - 1)
        str_nova += novo_car
    
    return str_nova


def eh_letra(car):
    return (ord('A') <= ord(car) <= ord('Z') or \
        ord('a') <= ord(car) <= ord('z'))


def dividir_str_em_2(strg):
    num_car = len(strg)
    mtde_car = int(num_car / 2)
    
    mtde_1 = strg[0:mtde_car]
    mtde_2 = strg[mtde_car:num_car]
    
    return mtde_1, mtde_2


main()