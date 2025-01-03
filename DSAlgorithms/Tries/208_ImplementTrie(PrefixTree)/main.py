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
# children["a"] = TrieNode() # when creating a node for the character a or inserting a node
class TrieNode:
  def __init__(self):
    self.children = {} # a hashmap since its easier, but we can also use array
    self.endOfWord = False # a variable to mark every single node as if it was the end of of word, initially it is False, we mark it True if it the end of a word

class Trie:

  def __init__(self):
    self.root = TrieNode() # our root is empty initially
  
  # Time Complexity: O(m), where m is the key length
  # Space Complexity: O(m), in the worst case, if newly inserted key doesn't share the same prefixes of existing keys in the trie, we have to add m new nodes, which takes O(m) space
  def insert(self, word):
    cur = self.root

    for c in word:
      if c not in cur.children: # if this character is not in our hashmap of children yet, it hasn't been inserted yet
        cur.children[c] = TrieNode() #key = character, value = TrieNode
      cur = cur.children[c] # if c exists, update cur and go to that node
    
    cur.endOfWord = True

  # Time Complexity: O(m) in each step of the algorithm we search for the next key character. In the worst case the algorithm perform m operations.
  # Space complexity: O(1), we just have the cur variable
  def search(self, word):
    cur = self.root
    for c in word:
      if c not in cur.children: # word does not exist
        return False
      cur = cur.children[c] # move ourselves to that child node of that character

    return cur.endOfWord # if this is set to true the word exists

  # Time Complexity: O(M), in each step we search for the next key character
  # Space Complexity: O(1)
  def startsWith(self, prefix):
    cur = self.root

    for c in prefix:
      if c not in cur.children:
        return False
      
      cur = cur.children[c]

    return True #we know there is a least one word that starts with the prefix

trie = Trie()
trie.insert("apple")