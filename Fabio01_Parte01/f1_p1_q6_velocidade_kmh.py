def main():
    velocidade_kmh = float(input('Digite um valor em km/h: '))

    velocidade_ms = calc_vel_ms(velocidade_kmh)

    print(f'O resultado é {velocidade_ms:.1f} m/s')


def calc_vel_ms(velocidade_kmh):
    velocidade_ms = velocidade_kmh / 3.6
    return velocidade_ms


main()
