# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
# one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
#
# You are given an integer array nums representing the data status of this set after the error.
#
# Find the number that occurs twice and the number that is missing and
# return them in the form of an array.
from collections import Counter
from typing import List

class Solution:

    # 此算法太费时间， nlogn
    # def findErrorNums(self, nums: List[int]) -> List[int]:
    #     replicate: int = -1
    #     loss: int = -1
    #     s = len(nums)
    #     print(s)
    #
    #     for index_s in range(1, s+1):
    #         if nums.count(index_s) == 2:
    #             replicate = index_s
    #         elif nums.count(index_s) == 0:
    #             loss = index_s
    #             print(loss)
    #
    #     return [replicate, loss]


    #v1： hash table 有意思
    # def findErrorNums(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     counterOfList = Counter(nums)
    #     result = [0,0]
    #     for i in range(1, n+1):
    #       if not counterOfList[i]:
    #           result[1] = i
    #       if counterOfList[i] == 2:
    #           result [0] = i
    #
    #     return result
    #V2: 同
    # def findErrorNums(self, nums: List[int]) -> List[int]:
    #   # most_common(1)[0][0]  is max. counter of counter list : [(6, 2)]
    #   return [Counter(nums).most_common(1)[0][0], (set(i for i in range(1, len(nums) + 1)) - set(nums)).pop()]



    #v3: set 数学方法，
      def findErrorNums(self, nums: List[int]) -> List[int]:
        n, sumSet = len(nums), sum(set(nums))
        # // 地板除
        return [sum(nums) - sumSet, n*(n+1)//2 - sumSet]


    #V4:

solution = Solution()
nums = [1,2,3,4,5,6,6]
# print((set(i for i in range(1, len(nums) + 1))- set(nums)))

# print(solution.findErrorNums(nums=nums))
