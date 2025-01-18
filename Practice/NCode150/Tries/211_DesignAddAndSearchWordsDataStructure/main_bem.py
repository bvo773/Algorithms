class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfWord = False

class WordDictionary:
  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word):
    curr = self.root
    for c in word:
      if c not in curr.children:
        curr.children[c] = TrieNode()
      curr = curr.children[c]
    
    curr.endOfWord = True
  
  def search(self, word):
    def dfs(trie, i):
      if i == len(word) - 1:
        if word[i] == '.':
          if word[i] not in trie.children:
            return False
          return dfs(trie)