"""
Implement a trie
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr_node = self.root
        for char in word:
            curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]

        curr_node.is_end_of_word = True

    def search(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return curr_node.is_end_of_word

    def starts_with(self, prefix):
        curr_node = self.root
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        return True

    """For returning words that have a given prefix"""
    def _dfs(self, prefix, words):
        pass


# trie = Trie()

# # Insert some words
# trie.insert("apple")
# trie.insert("banana")
# trie.insert("orange")

# # Search for some words
# print(trie.search("apple"))    # True
# print(trie.search("pear"))     # False

# # Check if there are any words starting with a prefix
# print(trie.starts_with("app")) # True
# print(trie.starts_with("pea")) # False


trie = Trie()

# Insert some words
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")
trie.insert("apricot")
trie.insert("avocado")

# Get autocomplete suggestions
suggestions = trie.starts_with("a")
print(suggestions) # ['apple', 'apricot', 'avocado']

suggestions = trie.starts_with("or")
print(suggestions) # ['orange']