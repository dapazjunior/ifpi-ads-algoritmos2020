def main():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    num3 = int(input('Digite o terceiro número: '))
    
    ordem = verificar_ordem(num1, num2, num3)
    
    print(f'A ordem é {ordem}')
  
   
def verificar_ordem(num1, num2, num3):
    if num1 > num2 and num2 > num3:
        ordem = num3, num2, num1
    elif num1 > num3 and num3 > num2:
        ordem = num2, num3, num1
    elif num2 > num3 and num3 > num1:
        ordem = num1, num3, num2
    elif num2 > num1 and num1 > num3:
        ordem = num3, num1, num2
    elif num3 > num2 and num2 > num1:
        ordem = num1, num2, num3
    else:
        ordem = num2, num1, num3
        
    
    return ordem

main()
