"""
Given a large Person array, sort people by age in ascending order.
"""
import numpy as np

class Person:
    def __init__(self, age):
        self.age = age

people = []
for _ in range(1000):
    people.append(Person(np.random.randint(0, 110)))

for i, p in enumerate(people):
    print(p.age)

    if i == 5:
        break

def bucket_sort(people_array):
    buckets = [[] for _ in range(110)]  # can't use [[]]*n syntax! python collection copy issue

    for p in people_array:
        buckets[p.age].append(p)

    sorted_people = []

    for bucket in buckets:
        for person in bucket:
            sorted_people.append(person)

    return sorted_people

sorted_people = bucket_sort(people)

print('\nAfter sorting:')
for i, sp in enumerate(sorted_people):
    print(sp.age)

    if i == 17:
        break