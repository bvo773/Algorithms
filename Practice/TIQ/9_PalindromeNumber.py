'''
Given an integer x, return true if x is a palindrome, and false otherwise

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: from left tro right, it reads -121. From right to left, it becomes
121-. Therefore it is not a palindrome.
'''

class Solution:

    # Easy Method: Converting it to a string
    
    def isPalindrome(self, x):
        num = str(x)

        i = 0
        j = len(num) - 1
        while i < j:
            if num[i] != num[j]:
                return False
            i+=1
            j-=1
        return True

sol = Solution()
print(sol.isPalindrome(-121))





