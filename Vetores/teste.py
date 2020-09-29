def num_divisores(num):
    div = 0
    
    for i in range(1, num + 1):
        if num % i == 0:
            div += 1
    
    print(div)


num_divisores(18)