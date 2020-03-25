# Entrada
#Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)

def main():
    velocidade_ms = float(input('Digite velocidade em m/s: '))

    velocidade_kmh = calcular_vel_kmh(velocidade_ms)

    print(f'A velocidade é {velocidade_kmh:.1f} km/h ')


def calcular_vel_kmh(velocidade_ms):
    velocidade_kmh = velocidade_ms * 3.6
    return velocidade_kmh

main()
