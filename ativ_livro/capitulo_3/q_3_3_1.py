def print_4_vezes(a):
    print(a)
    print(a)
    print(a)
    print(a)

def print_grade():
    extremidade = (('+ ' + 4*('- '))*2 + '+')
    entre = (('|' + 9*(' '))*2 + '|')
    print(extremidade)
    print_4_vezes(entre)
    print(extremidade)
    print_4_vezes(entre)
    print(extremidade)

print_grade()