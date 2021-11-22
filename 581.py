from typing import List
class Solution:
  def findUnsortedSubarray(self, nums: List[int]) -> int:
    sortedNums = sorted(nums)
    length = len(nums)
    start, end = -1, -1
    for i in range(length):
      if nums[i] != sortedNums[i]:
        start = i
        break
    for i in range(length):
      if nums[length - i - 1] != sortedNums[length - i - 1]:
        end = length - i - 1
        break
    if start == -1:
      return 0
    return end - start + 1
