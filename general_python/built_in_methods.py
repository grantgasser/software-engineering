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