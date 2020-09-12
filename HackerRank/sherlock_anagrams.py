def main():
    num_queries = int(input())
    
    for _ in range(num_queries):
        string = input()
        
        annagramatic_pairs = is_there_anagramas(string)
        print(annagramatic_pairs)


def all_substrings(string):
    index_fixed = 0
    substrings = []
    
    while index_fixed < len(string):
        index_float = 0
        
        while index_float < len(string):
            substring = string[index_fixed:index_float + 1]
            if substring != '':
                substrings.append(substring)
            
            index_float += 1
        
        index_fixed += 1
    
    return substrings


def is_there_anagramas(string):
    substrings = all_substrings(string)
    index_sub_fixed = 0
    num_anagramas = 0
    
    while index_sub_fixed < len(substrings):
        index_sub_float = 0
        
        while index_sub_float < len(substrings):
            if index_sub_float != index_sub_fixed:
                if compare_substrings(substrings[index_sub_fixed], substrings[index_sub_float]):
                    num_anagramas += 1
                
            index_sub_float += 1
        
        index_sub_fixed += 1
    
    return num_anagramas


def compare_substrings(str1, str2):
    conditions = 0
    
    if len(str1) == len(str2):
        conditions += 1
    
    for c in str1: