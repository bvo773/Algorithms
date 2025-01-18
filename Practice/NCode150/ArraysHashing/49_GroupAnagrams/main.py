"""Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram
is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters 
exactly once.

Example 1:
    Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]
"""


"""
Approach 1: Categorize by Sorted String

Intuition
Two strings are anagrams if and only if their sorted strings are equal

Algorithm
Maintian a map ans : {String -> List} where each key K is a sorted string, and each value is the list of strings from the initial input
when sorted, are equal to K.

In Java, we store the key as string, eg. code. In Python, we still store the key as hashable tuple, eg. ('c','o','d','e').
"""

class Solution:
    def groupAnagrams(self, strs):
        pass

my_tuple = ('c', 'o', 'd', 'e')
print(my_tuple)

for k,v in my_tuple:
    print(f"{k}, {v}")