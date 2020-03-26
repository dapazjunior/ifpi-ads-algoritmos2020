def main():
    nome_1 = input('Qual o nome do primeiro professor? ')
    qtde_aulas_1 = int(input(f'Qual o número de horas aulas dadas pelo professor {nome_1}? '))
    hora_aula_1 = float(input(f'Qual o valor da hora aula do professor {nome_1}? R$ '))
    
    nome_2 = input('Qual o nome do segundo professor? ')
    qtde_aulas_2 = int(input(f'Qual o número de horas aulas dadas pelo professor {nome_2}? '))
    hora_aula_2 = float(input(f'Qual o valor da hora aula do professor {nome_2}? R$ '))
    
    salario_1 = calcular_salario(qtde_aulas_1, hora_aula_1)
    salario_2 = calcular_salario(qtde_aulas_2, hora_aula_2)
    
    maior = comparar_salario(nome_1, salario_1, nome_2, salario_2)
    
    print(f'>>>>>>>> SALÁRIOS INFORMADOS <<<<<<<<\n\nProfessor {nome_1} receberá R$ {salario_1:.2f}')
    print(f'Professor {nome_2} receberá R$ {salario_2:.2f}\n\nPotanto, ', end = '')
    
    if maior == 0:
        print('os salários são iguais.')
    else:
        print(f'o professor {maior} tem o maior salário.')


def calcular_salario(aulas, hora_aula):
    salario = aulas * hora_aula
    return salario


def comparar_salario(nome1, salario1, nome2, salario2):
    if salario1 > salario2:
        return nome1
    if salario2 > salario1:
        return nome2
    else:
        return 0


main()
