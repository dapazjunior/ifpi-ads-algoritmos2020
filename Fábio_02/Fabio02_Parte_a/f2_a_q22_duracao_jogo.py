def main():
    horas_inicio = int(input('Qual o horário de início do jogo? (HH:MM)\nHoras:'))
    minutos_inicio = int(input('Minutos: '))
        
    horas_fim = int(input('Qual o horário de início do jogo? (HH:MM)\nHoras:'))
    minutos_fim = int(input('Minutos: '))
    
    print('A partida durou ', end='')
    calcular_duracao(horas_inicio, horas_fim, minutos_inicio, minutos_fim)
    
    
def calcular_duracao(horas_inicio, horas_fim, minutos_inicio, minutos_fim):
    tempo_inicio = horas_inicio * 60 + minutos_inicio
    
    tempo_fim = horas_fim * 60 + minutos_fim
    
    if tempo_fim < tempo_inicio:
        duracao = 24 * 60 - tempo_inicio + tempo_fim
        return print(f'{duracao // 60}:{duracao % 60}.')
    elif tempo_inicio < tempo_fim:
        duracao = tempo_fim - tempo_inicio
        return print(f'{duracao // 60}:{duracao % 60}.')


main()
