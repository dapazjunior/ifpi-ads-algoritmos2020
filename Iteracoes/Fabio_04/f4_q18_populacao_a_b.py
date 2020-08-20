def main():
    populacao_a = 200000
    cresc_a = 0.035
    populacao_b = 800000
    cresc_b = 0.0135
    anos = 0
    
    while populacao_a < populacao_b:
        populacao_a += populacao_a * cresc_a
        populacao_b += populacao_b * cresc_b
        
        anos += 1

    
    print(f'Após {anos} anos a população de A ultrapassará a de B')
    print(f'Poupulação A: {populacao_a:.0f}\nPopulação B: {populacao_b:.0f}')


main()
