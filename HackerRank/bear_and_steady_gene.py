def main():
    len_gene = int(input())
    gene = input()
    
    num_genes_changed = steady_gene(gene, len_gene)
    
    print(num_genes_changed)


def steady_gene(string, num):
    substrings = all_substrings(string)
    index = 0
    
    while index < len(substrings):
        substring = substrings[index]
        
        if len(substring) >= num/4:
            


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


main()