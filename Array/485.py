from typing import List
class Solution:
    def findMaxConsecutiveOnes(self,nums: List[int] ) -> int:
      count = max_count = 0
      for num in nums:
        if num == 1:
          count += 1
          if max_count < count:
            max_count = count
        else:
          count = 0
      return max_count


nums: List[int] = [1, 1, 0, 1, 1, 1]
soltion = Solution()
print(soltion.findMaxConsecutiveOnes(nums))

