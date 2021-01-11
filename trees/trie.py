"""
pg. 117

Trie (prefix tree): n-ary tree where characters are stored at each node and each path
down the tree may represent a word. A node can have 1 to (alphabet size + 1) children.

Commonly used to stroe entire English language for quick prefix lookups. While hash table
can quickly look up whether string is valid word, it cannot tell us if a string is a 
prefix of any valid works.
    => A trie can do this in O(K) where K is length of the string, fast!


Many problems involving lists of valid words leverage a trie as an optimization.
"""