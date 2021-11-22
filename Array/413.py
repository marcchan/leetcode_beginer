from typing import List

class Solution:
  def numberOfArithmeticSlices(self, nums: List[int]) -> int:
      n = len(nums)
      for i in range(n-1):
        for j in range(i+1,n):
          if j - i  > 2 &


solu = Solution()
solu.numberOfArithmeticSlices([1])
