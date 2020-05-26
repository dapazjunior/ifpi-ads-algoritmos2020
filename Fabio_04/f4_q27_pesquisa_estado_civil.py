def main():
    cont_pessoas = 0
    cont_mulheres = 0
    soma_idade_m = 0
    cont_homens = 0
    soma_idade_h = 0
    homens_solt = 0
    mulheres_solt = 0
    m_div_mais_de_30 = 0
    
    while cont_pessoas < 100:
        sexo = int(input('\nSEXO\n1 - Masculino\n2 - Feminino\n>>> '))
        idade = int(input('IDADE\n>>> '))
        estado_civil = int(input('ESTADO CIVIL\n1 - Casado\n2 - Solteiro\n3 - Divorciado\n4 - Viúvo\n>>> '))
        
        if sexo == 1:
            cont_homens += 1
            soma_idade_h += idade
            if estado_civil == 2:
                homens_solt += 1

        if sexo == 2:
            cont_mulheres += 1
            soma_idade_m += idade
            if estado_civil == 2:
                mulheres_solt += 1
            elif estado_civil == 3 and idade > 30:
                m_div_mais_de_30 += 1
        
        cont_pessoas += 1
    
    media_h = soma_idade_h / cont_homens
    media_m = soma_idade_m / cont_mulheres
    percent_h_solt = homens_solt / cont_homens * 100
    percent_m_solt = mulheres_solt / cont_mulheres * 100
    
    print(f'\nMÉDIA DE IDADE DOS HOMENS: {media_h:.1f} anos')
    print(f'MÉDIA DE IDADE DAS MULHERES: {media_m:.1f} anos')
    print(f'PERCENTUAL DE HOMENS SOLTEIROS: {percent_h_solt:.1f}% dos homens')
    print(f'PERCENTUAL DE MULHERES SOLTEIRAS: {percent_m_solt:.1f}% das mulheres')
    print(f'MULHERES DIVORCIADAS COM MAIS DE 30: {m_div_mais_de_30} mulheres')


main()
