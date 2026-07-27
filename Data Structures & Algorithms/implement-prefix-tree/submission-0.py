class TrieNode:
    def __init__(self):
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        self._tombstone = "*"
        

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                new_node = TrieNode()
                current_node.children[char] = new_node
                current_node = new_node
        current_node.children[self._tombstone] = None


    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return self._tombstone in current_node.children
        

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return True
        