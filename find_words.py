"""
Grant Gasser 
AI/ML Coding Exercise

Assumptions
    - alphabetic (26 letters)
    - lowercase letters
    - RxC grid formatted as 2D array of chars

Estimating Time Complexity of My Solution:
    - for loop is O(R x C) where R is rows and C is columns
        - BFS is O(|V| + |E|) => O(R*C + 8(R*C)) => O(R*C)
            - here we're assuming each vertex (letter) has 
            8 edges (neighboring letters), a conservative overestimate

    Total: O(R^2 x C^2)
"""

import nltk
from nltk.corpus import words

# getting our vocabulary/dictionary, 236736 words in the list
nltk.download('words')
vocab = words.words()

# 4x4
example = [['r', 'a', 'e', 'l'],
            ['m', 'o', 'f', 's'],
            ['t', 'e', 'o', 'k'],
            ['n', 'a' , 't', 'i']]

# 5x4
example2 = [['r', 'a', 'e', 'l'],
            ['m', 'o', 'f', 's'],
            ['t', 'e', 'o', 'k'],
            ['n', 'a' , 't', 'i'],
            ['t', 'l', 's', 'a']]

#7x5
example3 = [['g', 'a', 'e', 'l', 'y'],
            ['m', 'o', 'f', 's', 'e'],
            ['j', 'j', 'o', 'q', 'a'],
            ['n', 'a' , 'p', 'i', 'r'],
            ['n', 's', 's', 't', 'q'],
            ['n', 'i' , 'p', 'i', 'e'],
            ['x', 'o', 'u', 'm', 'c']]

def find_words(board, vocab):
    """
    Find words that can be formed by a sequence of 
    adjacent (top, bottom, left, right, diagonal) letters. Words must be >= 3 characters.

    Args:
        board (List[List[str]]): 2D array of characters representing the board
        vocab (List[str]): list of words (our dictionary/vocabulary)

    Returns:
        words (List[str]): list of found words
    """

    # clockwise starting from directly above
    possible_steps = [[-1, 0], [-1, 1], [0, 1], [1, 1], 
                    [1, 0], [1, -1], [0, -1], [-1, -1]]

    words = []

    # O(R x C) where R is rows and C is columns of input
    for i in range(len(board)):
        for j in range(len(board[0])):
            queue = [[i, j]]
            paths_queue = [[]]  # parallel to the actual queue
            visited = []

            # BFS but we're looking at all possible paths (words)
            while queue:
                curr = queue.pop(0)
                path = paths_queue.pop(0)

                if curr not in visited:
                    visited.append(curr)

                    # for each neighbor
                    for step in possible_steps:
                        new = [None, None]

                        # consider stepping to a new cell
                        new[0] = curr[0] + step[0]
                        new[1] = curr[1] + step[1]

                        # if the new cell is in bounds
                        if (new[0] >= 0) and (new[1] >= 0) and (new[0] <= len(board) - 1) \
                            and (new[1] <= len(board[0]) - 1):
                            queue.append(new)

                            # keep track of location of letters in the current path
                            new_path = []
                            for loc in path:
                                new_path.append(loc)
                            
                            # add current cell to path and append to the path queue
                            new_path.append(curr)
                            paths_queue.append(new_path)

                            # build up string based on path locations, ensure not duplicating cells
                            duplicate_cell = False
                            possible_word = ''
                            possible_word_path = []
                            for loc in new_path:
                                if loc in possible_word_path:
                                    duplicate_cell = True
                                else:
                                    possible_word_path.append(loc)
                                    possible_word += board[loc[0]][loc[1]]
                            
                            # check if the new loc is a duplicate
                            if new in possible_word_path:
                                duplicate_cell = True 
                            else:
                                possible_word_path.append(new)
                                possible_word += board[new[0]][new[1]]
                            
                            if not duplicate_cell:
                                # if the string is actually a word >=3 chars
                                if possible_word in vocab and len(possible_word) >= 3:
                                    # no repeats
                                    if possible_word not in words:
                                        words.append(possible_word)
    return words

print(find_words(example, vocab))