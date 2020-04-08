a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

triangulo = a * c / 2
print('TRIANGULO: {:.3f}'.format(triangulo))

pi = 3.14159
circulo = pi * c**2
print('CIRCULO: {:.3f}'.format(circulo))

trapezio = (a + b) * c / 2
print('TRAPEZIO: {:.3f}'.format(trapezio))

quadrado = b**2
print('QUADRADO: {:.3f}'.format(quadrado))

retangulo = a * b
print('RETANGULO: {:.3f}'.format(retangulo))