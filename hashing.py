"""
Hashing, O(1) lookup

k is keys, n is # of keys, m is len of table
want table to be O(n) in memory, so it can be 2N if needed, m = 2n

Common Hash Function: k mod m (best if m is prime and not close to powers of 2 or 10)
"""

names = ['Grant', 'John', 'Nick', 'Hannah', 'Mollie']

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class HashTable(object):
    def __init__(self):
        # based on estimated data size
        self.table = [None]*10

    def hash_func(self, name):
        ascii_sum = ord(name[0]) + ord(name[1]) + ord(name[2])
        idx = ascii_sum % len(self.table)
        return idx

    def put(self, name):
        idx = self.hash_func(name)
        if self.table[idx] == None:
            self.table[idx] = ListNode(name)
        else:
            # linear probing/hashing (linked list)
            curr = self.table[idx]
            while curr.next:
                curr = curr.next
            curr.next = ListNode(name)

    def get(self, name):
        idx = self.hash_func(name)
        if self.table[idx] == None:
            #raise KeyError('Key: {} does not exist in the hash table.'.format(name))
            return None
        else:
            curr = self.table[idx]
            while curr.val != name and curr:
                curr = curr.next

            if curr:
                return (idx, curr.val)
            else:
                #raise KeyError('Key: {} does not exist in the hash table.'.format(name))
                return None

    def rehash():
        temp = self.table.copy()
        self.table = [None]*2*len(self.table)

        # how to do without iterating all the way through temp? 

class Person(object):
    def __init__(self, name, age, sex):
        self.name = name 
        self.age = age 
        self.sex = sex 

class HashMap(HashTable):
    def __init__(self):
        super().__init__()
        
    def put(self, name, age, sex):
        idx = self.hash_func(name)
        
        # ignoring collisions for now
        self.table[idx] = Person(name, age, sex)

    def get(self, name):
        idx = self.hash_func(name)
        if self.table[idx] == None:
            #raise KeyError('Key: {} does not exist in the hash table.'.format(name))
            return None
        else:
            return (self.table[idx].name, self.table[idx].age, self.table[idx].sex)

# test HT
ht = HashTable()
print(ht.table)

for i in names:
    ht.put(i)

for i in names:
    print(ht.get(i))

print(ht.table[9].next.val)

# test HM
hm = HashMap()
print('\n\n')
hm.put('Grant', 24, 'M')
#hm.put('Nick', 23, 'M')
hm.put('Mollie', 23, 'F')
hm.put('Hannah', 23, 'F')

# change so no collisions because ignoring for now
names = ['Grant', 'Parm', 'Jazz', 'Hannah', 'Mollie']
for i in names:
    print('getting:', i)
    print(hm.get(i))