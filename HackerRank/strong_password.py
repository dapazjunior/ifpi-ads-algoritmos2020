def main():
    num_char = int(input())
    password = input()
    
    add_char = is_strong(num_char, password)
    
    print(add_char)


def is_strong(num, password):
    add_char = 0
    
    if is_there_lower(password) == False:
        add_char += 1
    
    if is_there_upper(password) == False:
        add_char += 1
    
    if is_there_number(password) == False:
        add_char += 1
    
    if is_there_special(password) == False:
        add_char += 1
        
    miss_char = is_there_6char(num, add_char)
    add_char += miss_char
    
    return add_char


def is_there_lower(string):
    count_lower = 0
    
    for c in string:
        if ord('a') <= ord(c) <= ord('z'):
            count_lower += 1
    
    if count_lower > 0:
        return True
    else:
        return False


def is_there_upper(string):
    count_upper = 0
    
    for c in string:
        if ord('A') <= ord(c) <= ord('Z'):
            count_upper += 1
    
    if count_upper > 0:
        return True
    else:
        return False


def is_there_special(string):
    special_characters = "!@#$%^&*()-+"
    
    count_special = 0
    
    for c in string:
        if c in special_characters:
            count_special += 1
    
    if count_special > 0:
        return True
    else:
        return False


def is_there_number(string):
    count_number = 0
    
    for c in string:
        if ord('0') <= ord(c) <= ord('9'):
            count_number += 1
    
    if count_number > 0:
        return True
    else:
        return False


def is_there_6char(num, add_char):
    if num + add_char >= 6:
        miss_char = 0
    else:
        miss_char = 6 - num - add_char
    
    return miss_char


main()
