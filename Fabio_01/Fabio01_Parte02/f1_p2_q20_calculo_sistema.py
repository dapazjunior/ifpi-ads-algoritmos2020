# Entrada
a = int(input('Digite o valro de "a": '))
b = int(input('Digite o valro de "b": '))
c = int(input('Digite o valro de "c": '))
d = int(input('Digite o valro de "d": '))
e = int(input('Digite o valro de "e": '))
f = int(input('Digite o valro de "f": '))

# Processamento
x = ((c * e) - (b * f)) / ((a * e) - (b * d))
y = ((a * f) - (c * d)) / ((a * e) - (b * d))

# Saída
print(f'O valor de x é {x}.')
