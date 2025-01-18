"""
Check if a string is a palindrome in O(n) time
:param s: the string to check
:return: True if the string is a palindrome, False otherwise
"""

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        # check if c is alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    
    return True

ex1 = "racecar"
ex2 = "12321"
ex3 = "1001"
print(f"isPalindrome: {is_palindrome(ex3)}")