class Solution:

  def searchInsert(self, nums, target):
    p1 = 0
    p2 = len(nums) - 1
    
    while p1 <= p2:
      mid = int((p1 + p2) / 2)

      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        p1 = mid + 1
      elif nums[mid] > target:
        p2 = mid - 1
    
    return -1


def main():
  print("Hello Leetcode World: 35 Search Insert position. \n")

  arr = [1, 3, 5, 6]
  target = 6
  test = Solution()

  print(test.searchInsert(arr, target))





if __name__ == "__main__":

  main()
