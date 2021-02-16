"""
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

O(3^N): 28ms, 86%
O(3^N): 14.3MB, 35%
"""

def letter_combinations(digits):
    if not digits:
        return []
    
    digits_to_letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    
    combinations = ['']
    for digit in digits:
        letters = digits_to_letters[digit]
        
        new_combinations = []
        for letter in letters:
            for i, combo in enumerate(combinations):
                new_combinations.append(combo + letter)
                
        combinations = new_combinations
        
    return combinations


print(letter_combinations('23'))