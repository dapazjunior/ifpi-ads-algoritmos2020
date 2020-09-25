def main():
    # Solicitar uma frase do usuário
    frase = input('Digite a frase: ')
    
    # Criptografar frase
    # 1 - Inverter frase
    # 2 - Substituir consoantes por '#'
    
    frase_encriptada = criptografar(frase)
    print(frase_encriptada)


def criptografar(string):
    string_invertida = inverter_str(string)
    string_final = substituir_consoantes(string_invertida)
    
    return string_final


def inverter_str(string):
    str_nova = ''  
    num_caractere = len(string)
    
    while num_caractere > 0:
        car_invertido = string[num_caractere - 1]
        str_nova += car_invertido
        
        num_caractere -= 1
    
    return str_nova


def substituir_consoantes(string):
    str_nova = ''
    
    for caractere in string:
        if eh_consoante(caractere):
            str_nova += '#'
        else:
            str_nova += caractere
    
    return str_nova


def eh_consoante(letra):
    if ord(letra) == 65 or ord(letra) == 69 or ord(letra) == 73 or ord(letra) == 79 \
        or ord(letra) == 85 or ord(letra) == 97 or ord(letra) == 101 or ord(letra) == 105 \
        or ord(letra) == 111 or ord(letra) == 117:
        return False
    else:
        return True


main()