from typing import List
from collections import Counter


class Solution:
  #执行用时：1820ms, 在所有 Python3提交中击败了10.62 %的用户内存消耗：16.5MB, 在所有 Python3提交中击败了18.06 %的用户
  # 很乱
  #   def findShortestSubArray(self, nums: List[int]) -> int:
  #       counterNums = Counter(nums)
  #       print(max(counterNums.values()))
        # maxFreqList = []
        # degree = 0
        # for (key, counter) in counterNums.most_common():
        #     if degree <= counter:
        #         degree = counter
        #         maxFreqList.append(key)
        # print(maxFreqList)
        # MaxlengthList = []
        # for maxFreqNum in maxFreqList:
        #     indexList = []
        #     for index, value in enumerate(nums):
        #         if value == maxFreqNum:
        #             indexList.append(index)
        #     MaxlengthList.append(indexList[degree - 1] - indexList[0] + 1)
        # return min(MaxlengthList)

  def findShortestSubArray(self, nums: List[int]) -> int:



soultion = Solution()
nums = [1, 2, 2, 3, 1]
# answer is 6
print(soultion.findShortestSubArray(nums))
