def print_4_vezes(a):
    print(a)
    print(a)
    print(a)
    print(a)

def print_grade():
    extremidade = (('+ ' + 4*('- '))*3 + '+')
    entre = (('|' + 9*(' '))*3  + '|' )
    print(extremidade)
    print_4_vezes(entre)
    print(extremidade)
    print_4_vezes(entre)
    print(extremidade)
    print_4_vezes(entre)
    print(extremidade)

print_grade()