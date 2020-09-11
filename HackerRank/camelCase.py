def main():
    string = input('')
    
    words = find_upper(string)
    
    print(words)


def find_upper(str):
    num_words = 1
    
    for c in str:
        if is_upper(c):
            num_words += 1
    
    return num_words


def is_upper(char):
    if ord('A') <= ord(char) <= ord('Z'):
        return True
    else:
        return False


main()
