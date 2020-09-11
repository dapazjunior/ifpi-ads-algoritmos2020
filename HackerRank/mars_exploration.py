def main():
    msg = input()
    num_char = len(msg)
    
    num_sos = num_char // 3
    sos = num_sos * 'SOS'
    
    letter_changed = verify_string(msg, sos)
    
    print(letter_changed)


def verify_string(msg, sos):
    index_sos = 0
    letters_changed = 0
    
    for c in msg:
        if c != sos[index_sos]:
            letters_changed += 1
        
        index_sos += 1
    
    return letters_changed
            

def verify_character(char1, char2):
    if char1 == char2:
        return True
    else:
        return False


main()
