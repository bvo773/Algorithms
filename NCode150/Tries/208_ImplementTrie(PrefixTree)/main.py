"""
A trie (pronounced as "try") or prefix tree is a data structure used to efficeitnly store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
  - Trie() Initializes the trie object
  - void insert(String word) Inserts the string word into the trie.
  - boolean search(String word) Returns true if the strong word in the trie (i.e, was inserted before), and false otherwise.

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
"""
class TrieNode:
  def __init__(self):
    self.children = {} # a hashmap since its easier, but we can also use array
    self.endOfWord = False # a variable to mark every single node as if it was the end of of word, initially it is False, we mark it True if it the end of a word
class Trie:

  def __init__(self):
    self.root = TrieNode()

  # Time Complexity: O(m), where m is the key length
  # Space Complexity: O(m), in the worst case, if newly inserted key doesn't share the same prefixes of existing keys in the trie, we have to add m new nodes, which takes O(m) space
  def insert(self, word):
    curr = self.root
    for c in word:
      if c not in curr.children:
        curr.children[c] = TrieNode()
      curr = curr.children[c]

    curr.endOfWord = True

  # Time Complexity: O(m) in each step of the algorithm we search for the next key character. In the worst case the algorithm perform m operations.
  # Space complexity: O(1), we just have the cur variable
  def search(self, word):
    curr = self.root
    for c in word:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    
    return curr.endOfWord
      
  # Time Complexity: O(M), in each step we search for the next key character
  # Space Complexity: O(1)
  def startsWith(self, prefix):
    curr = self.root
    for c in prefix:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    return True