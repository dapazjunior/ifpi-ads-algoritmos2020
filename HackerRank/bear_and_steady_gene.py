def main():
    len_gene = int(input())
    gene = input()
    
    if is_steady(gene, '', len_gene/4):
        num_genes_changed = 0
    else:
        num_genes_changed = steady_gene(gene, len_gene)
    
    print(num_genes_changed)


def steady_gene(string, num_nucleobases):
    max_nucleobases = num_nucleobases // 4
    start_index = 0
    final_index = start_index + 1
    len_sub = 1
    
    while len_sub < len(string):
        start_index = 0
        final_index = start_index + len_sub
        while start_index < len(string):
            substring = string[start_index:final_index]
            if len(substring) < len_sub:
                pass
            else:
                if is_steady(string, substring, max_nucleobases):
                    return len_sub
        
            start_index += 1
            final_index += 1
        
        len_sub += 1
        


def is_steady(gene, subgene, num):
    # ON ORIGINAL GENE
    num_A, num_T, num_G, num_C = count_nucleobses(gene)
    
    # ON MODIFIED SUBGENE
    removed_A, removed_T, removed_G, removed_C = count_nucleobses(subgene)
    
    if num_A - removed_A <= num and \
       num_T - removed_T <= num and \
       num_C - removed_C <= num and \
       num_G - removed_G <= num:
           return True
    else:
        return False


def count_nucleobses(gene):
    count_A = 0
    count_T = 0
    count_G = 0
    count_C = 0
    
    for c in gene:
        if c == 'A':
            count_A += 1
        elif c == 'T':
            count_T += 1
        elif c == 'G':
            count_G += 1
        elif c == 'C':
            count_C += 1
    
    return(count_A, count_T, count_G, count_C)


main()