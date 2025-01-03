"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
  -WordDictionary() Initializes the object.
  -void addWord(word) Adds word to the data structure, it can be matched later.
  -bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


# Insert TrieNode based on the correspond character
"""   

class TrieNode:
  def __init__(self):
    self.children = {} # a : TrieNode
    self.endOfWord = False

class WordDictionary:
  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word):
    cur = self.root
    for c in word:
      if c not in cur.children:
        cur.children[c] = TrieNode()
      cur = cur.children[c]

    cur.endOfWord = True
  
  def search(self, word):
    def dfs(j, root):
      cur = root
      for i in range(j, len(word)):
        c = word[i]
        # remember if we have a dot, potentially we got down 26 different paths, the dot can match any of the 26 characters. We will use backtracking or recursion, hard to do it iteractively
        if c == ".": # recursive case if we have a dot
          for child in cur.children.values(): # we get the children nodes in the map
            if dfs(i+1, child): #we are skippinh the dot, so we have to do i + 1
              return True
          return False
        else:
          if c not in cur.children:
            return False
          cur = cur.children[c] # shift our pointer to that node if the character exists

      return cur.endOfWord
    
    return dfs(0, self.root)
  

        

dictionary = WordDictionary()
dictionary.addWord("pad")
dictionary.printChildren()
