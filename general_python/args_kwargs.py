"""
*args

When we don't know how many arguments we are passing. The arguments
are stored in a tuple.

def foo(*args):
    print(args)

foo(1, 2, 3) # output: (1, 2, 3)
"""

def apply_operation(operation, *numbers):
    result = []
    for number in numbers:
        result.append(operation(number))
    return result

def cube(x):
    return x**3


print(apply_operation(lambda x: x**2, 2, 3, 4, 5))

print(apply_operation(cube, 2, 3, 4))

"""
*kwargs

When we don't know how many KEYWORD arguments we are passing. The arguments
are stored in a DICTIONARY.

def bar(**kwargs):
    print(kwargs)

bar(a=1, b=2, c=3) # output: {'a': 1, 'b': 2, 'c': 3}
"""

def format_name(fname, lname, **kwargs):
    """Formats a name string based on different arguments given"""
    middle_initial = kwargs.get('middle_initial', False)
    if middle_initial:
        name = f"{fname} {middle_initial}. {lname}"
    else:
        name = f"{fname} {lname}"

    title = kwargs.get('title', False)
    if title:
        name = f"{title} {name}"
    
    return name

print(format_name("Brad", "Pitt", middle_initial='L', title='Sir'))
print(format_name("Angelina", "Jolie", title='Mrs.'))