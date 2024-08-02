# https://www.w3schools.com/python/python_ref_string.asp

# capitalize()
print('\ncapitalize()')
print('grant'.capitalize())

# lower()
print('\nlower()')
print('GRANT'.lower())

# upper()
print('\nupper()()')
print('Grant'.upper())

# count()
print('\ncount()()')
print('na na na'.count('na')) # 3
print('Grant'.count('g')) # 0
print('grant'.count('g')) # 1

# endswith()
print('\nendswith()')
print('this is a STOP'.endswith('STOP'))

# find()
print('\nfind()')
print('This is a test'.find('i'))  # 2 - first occurence

# isalnum()
print('\nisalnum()')
print('123ABC'.isalnum())
print('123.ABC'.isalnum())

# isalpha()
print('\nisalpha()')
print('123ABC'.isalpha())
print('grant'.isalpha())

# isdigit()
print('\nisdigit()')
print('123'.isdigit())
print('grant12'.isdigit())

# replace()
print('\nreplace()')
print('123'.replace('1', '0'))

# split()
print('\nsplit()')
print('602-282-1042'.split('-'))

# strip()
print('\nstrip()')
stripped = 'messy input     \t'.strip()
for s in stripped:
    print(s)

# zfill()
print('\nzfill()')
print('50'.zfill(4))

