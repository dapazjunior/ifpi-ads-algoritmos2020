def main():
    x1 = float(input('Primeiro vértice:\nx = '))
    y1 = float(input('y = '))
    
    # Para que dois pontos definam um retângulo eles precisam ser opostos!
    x2 = float(input('\nVértie oposto:\nx = ')) 
    y2 = float(input('y = '))
    
    area = calcular_area(x1, x2, y1, y2)
    
    print(f'A area do retângulo é {area}.')

def calcular_area(x1, x2, y1, y2):
    ladox = x2 - x1
    ladoy = y2 - y1
    
    area = ladox * ladoy
    if area > 0:
        return area
    elif area < 0:
        area = (-1) * area
        return area
    else:
        return 'nula'
      
    
main()
