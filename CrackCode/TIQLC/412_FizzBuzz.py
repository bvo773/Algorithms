"""
412. Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.


Algorithm
- Initialize an empty answer list.
- Iterate on the numbers from 1...N.
- For every number, if it is divisible by both 3 and 5, add FizzBuzz to the answer list.
- Else, Check if the number is divisible by 3, add Fizz.
- Else, Check if the number is divisible by 5, add Buzz.
- Else, add the number

Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def fizzBuzz(self, n):
        arr = []
        for i in range(1, n + 1):
            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)
            if divisible_by_3 and divisible_by_5:
                arr.append("FizzBuzz")
            elif divisible_by_3:
                arr.append("Fizz")
            elif divisible_by_5:
                arr.append("Buzz")
            else:
                arr.append(str(i))
        
        return arr


sol = Solution()
print(sol.fizzBuzz(5))