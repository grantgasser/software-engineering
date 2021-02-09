"""
208. Implement Trie (Prefix Tree)
Medium

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

"""
188ms, 52%
32MB, 44%
"""
class Node:
    def __init__(self, letter, is_end_word=False):
        self.letter = letter
        self.children = {}
        self.is_end_word = is_end_word

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        
        Insert is O(N) where N is size of word
        """
        parent = self.root
        for letter in word:
            # does parent have this letter as a child?
            child = parent.children.get(letter)
            
            # if not, create new one
            if not child:
                child = Node(letter)
            
                # point parent to child
                parent.children[letter] = child
                
            # move down the trie
            parent = child
            
        # set flag of last node indicating end of word
        parent.is_end_word = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the WORD is in the trie.
        
        Search is O(N) where N is size of word
        """
        curr_node = self.root
        for letter in word:
            # does curr have this letter as a child?
            next_node = curr_node.children.get(letter)
            
            if next_node:
                # keep going
                curr_node = next_node
            else:
                return False
            
        # not looking for prefix (is string in trie, but an actual word!)
        # need to check if last node is the end of a word
        if curr_node.is_end_word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        
        startsWith is O(K) where K is size of prefix
        """
        curr_node = self.root
        for letter in prefix:
            # does curr have this letter as a child?
            next_node = curr_node.children.get(letter)
            
            if next_node:
                # keep going
                curr_node = next_node
            else:
                return False
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)