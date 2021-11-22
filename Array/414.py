from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ## use sorted with complexity with O(nlogn)
        # if len(nums) < 1 | len(nums) > 10 ** 4:
        #       return -1
        # nums_sorted_set = sorted(set(nums), reverse= True)
        # return nums_sorted_set[2] if len(nums_sorted_set) >= 3 else nums_sorted_set[0]
        #
        ## use set(nums) must be cost space complexity O(n)
        ## maintain three values or a set with length 3 is the best solution of this task
        ## maintain a 3 values set must be use max/ min, think maintain three values is the best

        first_num = second_num = third_num = float("-inf")  # 负无穷大
        for num in nums:
          if num > third_num:
            if num > second_num:
              if num > first_num:
                third_num = second_num
                second_num = first_num
                first_num = num
              elif num < first_num:
                third_num = second_num
                second_num = num
            elif num < second_num:
              third_num = num
        return third_num if third_num != float("-inf") else first_num

solution = Solution()
nums: List[int] = [1,-2147483648,2]
solution.thirdMax(nums= nums)
