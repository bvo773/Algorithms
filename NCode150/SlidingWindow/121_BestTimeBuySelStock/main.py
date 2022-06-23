def maxProfit(self, prices: List[int]) -> int:
  #We need to find the maximum difference (which will be the maxiumum profit) between two numbers in the given array. Also, the second number(selling price) must be larger than the first one (buying price).
  #In formal termins, we need to find max(prices[j] - prices[i]), for every i and j such that j > i    
  
  # Brute Force: for each day we calculate every next days and compare each day if the current profit > max profit, if it is we assigned to a new max profit.
  # Time Complexity: O(N^2). Loops run n(n-1)/2 times
  # Space Complexity: O(1). Only two variables - maxprofit and profit are used
  '''
  max_profit = 0
  for i in range(len(prices)):
      for j in range(i + 1, len(prices)):
          profit = prices[j] - prices[i]
          if profit > max_profit:
              max_profit = profit
  
  return max_profit
  '''
  
  # One-Pass
  # Time Complexity O(N) where N is the length of prices
  # Space Complexity O(1)
  # Algorithm: Two pointers with sliding window left and right pointer, we buy low on the left pointer and sell high with the right pointer
  l, r = 0, 1 #l - buy r - sell
  maxProfit = 0
  
  while r < len(prices):
    if prices[l] < prices[r]:
      profit = prices[r] - prices[l]
      maxProfit = max(maxProfit, profit)
    else:
      l = r

    r += 1
      
  return maxProfit

  
