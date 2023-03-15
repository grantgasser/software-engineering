"""
3/15
"""

"""
he said it verbally, i wrote this:

function that takes expression (5 + 3), mult, div, add, sub

numbers can be multiple digits, also negatives

spaces where spaces are valid (but not within numbers)

5+3

return
  result as number
  
operand in [+, -, /, *]

f("33") -> 33
  
f("5 + 3") -> 8
f("5-3") -> 2
f("2*4") -> 8

f("-2 * 5") -> -10
f("15 / 3") -> 5

"x operand y operand z ..."

f("5 + 2 * 5 / 2") -> 10

2,5 * res1

res1 / 2

5 + res2

{
    "*": (2, 5),
    "/": (5, 2)
}

PEMDAS 
"""

# TODO: did not finish
def evaluate(expression):
    res = 0
    
    # Remove trailing 
    expression = expression.strip()
    
    i = 0
    while i < len(expression):
        char = expression[i]
        if char == '-':
            # todo
            pass
        
        elif char.isdigit():
            j = i + 1
            while j < len(expression) and expression[j].isdigit():
                j += 1
                
            x = expression[i:j]
            i = j
          
        else:
            if char == '*':
                pass
            elif char == '/':
                pass
                
            i += 1
                    
    
    return res
    
print(evaluate("33"))
print(evaluate(" 5 + 3"))


"""
Yikes. Was able to parse first number, started parsing operand but didn't get around to it...

Couldn't think of proper way to parse where there are several operands and do PEMDAS. Settled on 

1st pass: take care of multiply/divide, store intermediate values
2nd pass: do add/subtract and use intermediate values

seemed very hacky, lots of edge cases, hard to come up with a nice general solution
"""