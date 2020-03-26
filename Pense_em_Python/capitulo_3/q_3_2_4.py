def do_twice(f, a):
    f(a)
    f(a)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'spam')
