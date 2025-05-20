from typing import List
from collections import defaultdict

'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
    Input: strs = ["act","pots","tops","cat","stop","hat"]
    Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
    Input: strs = ["x"]
    Output: [["x"]]

Example 3:
    Input: strs = [""]
    Output: [[""]]

Constraints:
    1 <= strs.length <= 1000.
    0 <= strs[i].length <= 100
    strs[i] is made up of lowercase English letters.

    
HINTS":
We can simply use an array of size O(26), since the character set is a through z (26 continuous characters), 
to count the frequency of each character in a string. Then, we can use this array as the key in the hash map to group the strings.
'''

class Solution:
    # 1) Sorting
    # Brute force solution, create a hashmap
    # Key: Tuple sorted string
    # Value: List of values with the same sorted anagram
    # Return a list of lists where each inner list contains words that are anagram of each other
    # Space Complexity O(M x N) -> M - The number of strings in the input list (strs)
    # Time Complexity O(M x N log N) N -> The average length of the strings
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            res[key].append(s)
        return list(res.values())

    # 2) Hash Table
    #  strs: A list of strings to be grouped
    #  returns a list of lists, where each inner list contains strings that are anagrams
    #  runtime: O(M x N) where M is the strings in the list, and N is the avg. length of each string
    #  space complexity: O(M x N)
    def groupAnagramsB(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #map charCount to list of Anagrams
        for s in strs:
            count = [0] * 26
            for c in s: # O(N) for eacj string s, count the characters frequencies where N is the avg. length of the strings
                count[ord(c) - ord('a')] += 1
            key = tuple(count) # O(26) = O(1)
            res[key].append(s)
        return list(res.values())

    def groupAnagramsTest(self, strs: List[str]) -> List[List[str]]:
        res 
        
strs = ["act","pots","tops","cat","stop","hat"]
solution = Solution()
print(solution.groupAnagrams(strs))