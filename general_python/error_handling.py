# Vanilla
try:
    print(x)
except:
    print('An exception has occured.')


# A specific type of error
try:
    print(y)
except NameError:
    print('A NameError has occured.')
except:
    print('Some other error has occurred.')

# Else (for when no error occurs)
try:
    print('Hello')
except:
    print('An error occured')
else:
    print('No error occurred')

# Finally (regardless of error or no error)
try:
    print('Hello')
except:
    print('Error')
finally:
    print('`Finally` block runs whether the was error or not.')

# Raise an exception
a = -1
if a < 0:
    # comment out so the rest of the program can run
    # raise Exception(f'a is less than 0: {a}')
    pass

b = "hello"
# even though type(b) returns <class 'str'>, you can check `is int`, `is str`
if not type(b) is int:
    #raise TypeError(f'Variable is not an int. value={b}, type={type(b)}')
    pass

if type(b) is str:
    print(f'variable is a string: value={b}, type={type(b)}')


"""Can catch an AssertionError"""
import sys

try:
    assert 'linux' in sys.platform
except AssertionError:
    print('This code only runs on linux')

# Regular assert syntax: `assert condition, error message`
assert 'darwin' in sys.platform, 'this is not a Mac'

# Another
try:
    cout << 'hello' << endl;
except:
    print('There was an error')


"""Creating custom Exception by inheriting from Exception"""
class InvalidAgeException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


MIN_AGE = 18
age = 17

try:
    if age < MIN_AGE:
        raise InvalidAgeException(f'Age is less than the minimum: {age} < {MIN_AGE}')
except Exception as e:
    print(type(e))
    print(e)