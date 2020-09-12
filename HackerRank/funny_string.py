def main():
    num_queries = int(input())
    
    while num_queries > 0:
        string = input()
        
        if is_funny(string):
            print('Funny')
        else:
            print('Not Funny')
        
        num_queries -= 1


def is_funny(string):
    reverse_str = reverse(string)
    
    difference_str = calc_difference(string)
    difference_reverse = calc_difference(reverse_str)
    
    if difference_str == difference_reverse:
        return True
    else:
        return False


def reverse(string):
    str_nova = ''  
    num_caractere = len(string)
    
    while num_caractere > 0:
        car_invertido = string[num_caractere - 1]
        str_nova += car_invertido
        
        num_caractere -= 1
    
    return str_nova


def calc_difference(string):
    difference = []
    
    index_str = 0
    
    while index_str < (len(string) - 1):
        diff = abs(ord(string[index_str]) - ord(string[index_str + 1]))
        difference.append(diff)
        
        index_str += 1
    
    return difference


main()
