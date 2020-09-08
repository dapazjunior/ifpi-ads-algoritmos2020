def main():
    hi, hf = input().split(' ')
    hi = int(hi)
    hf = int(hf)
    
    if hi > hf:
        tempo = 24 - hi + hf
    elif hf > hi:
        tempo = hf - hi
    else:
        tempo = 24
    
    print('O JOGO DUROU {} HORA(S)'.format(tempo))

main()
