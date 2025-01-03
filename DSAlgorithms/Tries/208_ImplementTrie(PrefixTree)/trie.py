"""
A trie (pronounced as "try") or prefix tree is a data structure used to efficient store and retrieve keys in a dataset of strings.
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
    self.children = {}
    self.endOfWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode()
  
  def insert(self, word):
    curr = self.root

    for c in word:
      if c not in curr.children:
        curr.children[c] = TrieNode()
      curr = curr.children[c]
    
    curr.endOfWord = True
  
  def search(self, word):
    curr = self.root
    for c in word:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    
    return curr.endOfWord

  def startsWith(self, prefix):
    curr = self.root

    for c in prefix:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    
    return True

  def printRootWords(self):
    
    def dfs(child):
      nonlocal word
      if not child:
        return
      
      for c in child.children:
        word += c
        dfs(child = child.children[c])

    curr = self.root
    for child in curr.children.keys():
      word = child
      dfs(curr.children[child])
      print(word)
    

    
      
      
  
trie = Trie()
trie.insert("apple")
trie.insert("bee")
trie.insert("cat")
print(trie.search("bee"))
trie.printRootWords()

