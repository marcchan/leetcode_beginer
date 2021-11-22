from typing import List
class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    n = len(nums)
    print(nums)
    for num in nums:
      x = abs(num) -1
      if nums[x] > 0: nums[x] *= -1
    print(nums)
    return [i+1 for i in range(n) if nums[i] > 0]


ex = Solution()
nums: List[int] = [4,3,2,7,8,2,3,1]
# nums: List[int] = [1,1]
print(ex.findDisappearedNumbers(nums))
