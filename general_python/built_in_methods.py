# https://www.w3schools.com/python/python_ref_functions.asp

# abs()
print('abs()')
print(abs(-5))

# all()
print('\nall()')
print(all([1, 1, 1, 0, 1]))
print(all([1, 1, 1, 1, 1]))
print(all([True, True]))

# any()
print('\nany()')
print(any([0, 0, 0]))
print(any([0, 0, 1]))
print(any([True, False]))

# bin()
print('\nbin()')
print(bin(4))
print(bin(1))

# chr()
print('\nchr()')
print(chr(70))

# ord()
print('\nord()')
print(ord('F'))

# eval() - probably what chatgpt does
print('\neval()')
print(eval("2 + 2"))
eval("print('test eval')")

# exec() - like eval() but can accept a large block of code, unlike eval() which only accepts single expr
print('\nexec()')
exec("name = 'Grant'\nprint(name)")

# filter(function, iterable)
print('\nfilter()')
filtered_arr = filter(lambda x: True if x > 0 else False, [-1, -7, 1, 0, 10])
print([x for x in filtered_arr])

# globals()
print('\nglobals()')
print(globals())

# hash()
print('\nhash()')
print(hash('Grant'))

# hex()
print('\nhex()')
print(hex(16))

# id()
print('\nid()')
print(id(filtered_arr))  # unique id/memory address for this object

# isinstance()
print('\nisinstance()')
print(isinstance(16, int))
print(isinstance([16], bool))
print(isinstance([16], list))

# map() - similar to filter() (FYI map and filter return iterables)
print('\nmap()')
print([x for x in map(lambda name: len(name), ['Grant', 'Tom', 'Barry'])])

# max() - also min()
print('\nmax()')
print(max([-1, -4, 11]))

# open()
print('\nopen()')
with open('demofile.txt', 'r') as f:
    text = f.read()
print(text.split('\n\n'))

# range()
print('\nrange()')
for i in range(5):
    print(i)
print()
for evens in range(0, 12, 2):
    print(evens)

# reversed()
print('\nreversed()')
print([r for r in reversed([1,2,3,4,5])])
print([r for r in reversed(range(1, 6, 1))])

# round()
print('\nround()')
print(round(5.5))
print(round(0.2))

# sorted()
print('\nsorted()')
print(sorted([-1, -5, 3, 8, 2]))
dic = {'the': 12, 'a': 14, 'an': 11, 'is': 24}
print(sorted(dic, key=dic.get, reverse=True)) # most frequent words

# sum()
print('\nsum()')
print(sum([1, 2, 3, 4, -4]))

# type
print('\ntype()')
print(type(dic))

# zip()
print('\nzip()')
one = ('a', 'b')
two = ('c', 'd')
for o, t in zip(one, two):
    print(o, t)
