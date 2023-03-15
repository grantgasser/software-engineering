"""
3/15

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example, Assume that  words = ["elephant", "zebra", "lion", "giraffe", "zebra"] .

["elephant", "zebra", "lion", "elephant", "giraffe", "zebra"]

e = 3
g = 4
d = 1

Given  word1 = "giraffe" ,  word2 = "elephant" , return 3. Given  word1 = "zebra" ,  word2 = "giraffe" , return 1.


FIRST THOUGHT: store in map, but then interviewer redirected me to just iterating thru list... duh
{
    elephant: [0],
    zebra: [1, 4]
    lion: [2],
    giraffe: [3, 7, 12, 15, 18, ...]
}

- this does not do well with dups
- but it might be a good idea if we're repeatedly calling f(word1, word2) and we're not too concerned
w/ dups
- precompute the map and then we don't have to iterate through the list each time we call f(word1, word2) 
"""

# I talked about various inputs but he said its OK to assume list has at least word1, word2
def shortest_dist(words, word1, word2):
    # Initialize
    min_dist = float('inf')
    most_recent_idx_word1 = None 
    most_recent_idx_word2 = None
    
    # Iterate and check words
    for i, word in enumerate(words):
        if word == word1:
            most_recent_idx_word1 = i
            
            # Had a bug here (`if most_recent_idx_word2`, failed when most_recent_idx_word2==0)
            # Added `is not None` after a little bit of logging
            if most_recent_idx_word2 is not None:
                min_dist = min(min_dist, abs(most_recent_idx_word2 - most_recent_idx_word1))
            
        elif word == word2:
            most_recent_idx_word2 = i
            
            if most_recent_idx_word1 is not None:
                min_dist = min(min_dist, abs(most_recent_idx_word2 - most_recent_idx_word1))
    
    return min_dist


print(shortest_dist(["elephant", "zebra", "lion", "giraffe", "zebra"], "giraffe", "elephant"))
print(shortest_dist(["elephant", "zebra", "lion", "giraffe", "zebra"], "zebra", "giraffe"))
