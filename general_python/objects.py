"""
Overriding __str__
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Jane", 33)
print(p1)
print('-'*30, '\n')

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person object instance: {self.name}, {self.age}"
    
p2 = Person2("Jane", 33)
print(p2)
print('-'*30, '\n')

"""
Overriding __repr__

Note __ indicates special method that is built-in
"""
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    def print_info(self):
        print(self.name, self.age)
    
p3 = Person3("Jill", 22)
print('Repr p1:', repr(p1))
print('Repr p3:', repr(p3))
print('-'*30, '\n')

"""
Inheritance
"""
class Student(Person3):
    def __init__(self, name, age):
        # super() will make the child class inherit all the methods and properties
        super().__init__(name, age)

        # Add a new properties
        self.grad_year = 2020

    def welcome(self):
        print('Welcome', self.name, 'to the class of', self.grad_year)

bob = Student('Bob', 22)
bob.print_info()
bob.welcome()
print('-'*30, '\n')

