# https://www.w3schools.com/python/python_ref_list.asp

# clear()
print('\nclear()')
foo = [1,2,3]
foo.clear()
print(foo)

# count()
print('\nclear()')
bar = [1,2,3,2]
print(bar.count(2))

# index()
print('\nindex()')
print([1,2,3,4].index(4))  # 3
#print([1,2,3,4].index(5))  # raises ValueError

# insert()
print('\ninsert()')
baz = [1,2,3,4]
baz.insert(2, -100)
print(baz)  # [1,2,-100,3,4]

# pop()
print('\npop()')
print('returns removed value:', baz.pop())  # 4
print(baz)  # [1,2,-100,3]

# remove() - inverse of insert()
print('\nremove()')
print('doesnt return value:', baz.remove(2))  # None
print(baz)  # [1, -100, 3]

# reverse() - inplace
print('\nreverse()')
arr = [1,2,3,4]
arr.reverse()
print(arr)

# or can use a built-in: reversed()
print([r for r in reversed(arr)])

# sort()
print('\nsort()')
arr.sort()
print(arr)

# or can use built-in: sorted()
print(sorted(arr))