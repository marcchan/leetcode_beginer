from typing import List
class Solution:
  def findDuplicates(self, nums: List[int]) -> List[int]:
    n = len(nums)
    for num in nums:
      # x = (num -1)%n
      nums[(num -1)%n] += n
    print(nums)
    return [i + 1 for i in range(n) if nums[i] > 2*n]

ex = Solution()
nums: List[int] = [4,3,2,7,8,2,3,1]
# nums: List[int] = [1,1]
print(ex.findDuplicates(nums))
