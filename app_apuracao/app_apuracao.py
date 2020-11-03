import json
import os


def main():
    # Coletar dados
    coligacoes = ler_coligacoes()
    candidatos = ler_apuracao()

    # Selecionar opção
    menu = criar_menu()
    input(menu)

    # Total de votos válidos
    votos_validos = verificar_votos_validos(candidatos)
    print(f'Total de votos válidos: {votos_validos}')
    
    input('\n<enter> para continuar...\n')

    # Cálculo do Quociente eleitoral
    quociente_eleitoral = calcular_qe(candidatos, 29)
    print(f'Quociente eleitoral: {quociente_eleitoral}')
    
    input('\n<enter> para continuar...\n')

    # Apuração dos Votos
    apuracao(coligacoes, candidatos)
    
    input('\n<enter> para continuar...\n')
    
    # Lista de vereadores eleitos
    verificar_eleitos(coligacoes, candidatos)
    
    input('\n<enter> para continuar...\n')

    # Lista de vereadores que seriam eleitos sem o voto proporcional
    verificar_eleitos_maioria(candidatos)

    input('\n<enter> para continuar...\n')

    print('Obrigado por usar nosso App')


def criar_menu():
    menu = '# # # APURAÇÃO DE VOTOS # # #\n'
    menu += 'Pressione enter após cada operação\n'
    menu += '1 - Total de votos válidos\n'
    menu += '2 - Quociente eleitoral\n'
    menu += '3 - Dados da Apuração\n'
    menu += '4 - Lista de vereadores eleitos\n'
    menu += '5 - Vereadores eleitos sem eleição proporcional\n'
    menu += '6 - Finalizar Programa\n'
    menu += '\n<enter> para continuar...\n'

    return menu


def verificar_votos_validos(candidatos):
    votos = 0
    
    for candidato in candidatos:
        votos += int(candidato['votos'])
    
    return votos


def calcular_qe(candidatos, vagas):
    votos = verificar_votos_validos(candidatos)
    qe = votos // vagas

    return qe


def soma_votos_coligacao(coligacoes, candidatos):
    for coligacao in coligacoes:
        for candidato in candidatos:
            if candidato['coligacao'] == coligacao['coligacao']:
                coligacao['total_votos'] += candidato['votos']


def calcaular_qp(coligacoes, candidatos):
    qe = calcular_qe(candidatos, 29)
    for coligacao in coligacoes:
        coligacao['qtd_vagas'] = coligacao['total_votos'] // qe
        coligacao['votos_sobra_total'] = coligacao['total_votos'] % qe


def calcular_vagas_sobra(coligacoes, vagas_sobra):
    for coligacao in coligacoes:
        fator_sobra = coligacao['votos_sobra_total'] / (coligacao['qtd_vagas'] + 1)
        coligacao['fator_sobra'] = fator_sobra
    
    coligacoes.sort(key = lambda c:c['fator_sobra'], reverse=True)
    
    cont = 0
    while vagas_sobra > 0:
        coligacoes[cont]['qtd_vagas'] += 1
        
        cont += 1
        vagas_sobra -= 1


def apuracao(coligacoes, candidatos):
    # Verificar a quantidade de votos por coligação
    soma_votos_coligacao(coligacoes, candidatos)
    print('# # # VOTOS POR COLIGAÇÃO # # #')
    for coligacao in coligacoes:
        print(coligacao['coligacao'], ':', coligacao['total_votos'])

    input('\n<enter> para contiuar...\n')

    # Calcular total de vagas por coligação("Quociente Partidário")
    vagas_preenchidas = 0
    calcaular_qp(coligacoes, candidatos)
    print('\n# # # VAGAS POR COLIGAÇÃO - SEM SOBRAS # # #')
    for coligacao in coligacoes:
        print(coligacao['coligacao'], ':', coligacao['qtd_vagas'])
        vagas_preenchidas += coligacao['qtd_vagas']

    print(f'Vagas preenchidas: {vagas_preenchidas}')

    input('\n<enter> para contiuar...\n')

    # Calcular vagas de sobra
    vagas_sobra = 29 - vagas_preenchidas
    vagas_preenchidas = 0
    calcular_vagas_sobra(coligacoes, vagas_sobra)
    print('\n# # # VAGAS POR COLIGAÇÃO - COM SOBRAS # # #')
    for coligacao in coligacoes:
        print(coligacao['coligacao'], ':', coligacao['qtd_vagas'])
        vagas_preenchidas += coligacao['qtd_vagas']

    print(f'Vagas preenchidas: {vagas_preenchidas}')


def verificar_eleitos(coligacoes, candidatos):
    print('# # # CANDIDATOS ELEITOS # # #')
    candidatos.sort(key=lambda x: x['votos'], reverse=True)
    cont_eleitos = 1
    for candidato in candidatos:
        for coligacao in coligacoes:
            if candidato['coligacao'] == coligacao['coligacao']:
                if coligacao['qtd_vagas'] > 0:
                    print(f'{cont_eleitos} -', candidato['nome'], '-', candidato['numero'])
                    cont_eleitos += 1
                    coligacao['qtd_vagas'] -= 1



def verificar_eleitos_maioria(candidatos):
    print('# # # CANDIDATOS ELEITOS (POR MAIORIA) # # #')
    candidatos.sort(key=lambda x: x['votos'], reverse=True)
    cont_eleitos = 0
    while cont_eleitos < 29:
        print(f'{cont_eleitos + 1} -', candidatos[cont_eleitos]['nome'], candidatos[cont_eleitos]['numero'])
        cont_eleitos += 1


def ler_coligacoes():
    arquivo = open('coligacoes.csv')
    coligacoes = []

    for linha in arquivo:
        coligacao = {}
        coligacao['coligacao'] = linha.strip()
        coligacao['total_votos'] = 0
        coligacao['qtd_vagas'] = 0
        coligacao['votos_sobra_total'] = 0
        coligacoes.append(coligacao)
    
    return coligacoes


def ler_apuracao():
    arquivo = open('apuracao.csv')
    candidatos = []

    for dado in arquivo:
        candidato = {}
        linha = dado.strip()
        info_candidato = linha.split(';')

        candidato['nome'] = info_candidato[0]
        candidato['numero'] = info_candidato[1]
        candidato['partido'] = info_candidato[2]
        candidato['coligacao'] = info_candidato[3]
        candidato['votos'] = int(info_candidato[4])

        candidatos.append(candidato)
    
    return candidatos


main()