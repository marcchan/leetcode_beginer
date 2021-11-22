# Given an integer array nums, design an algorithm to randomly shuffle the array. 
# All permutations of the array should be equally likely as a result of the shuffling.

# Implement the Solution class:

# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.

# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。

# 实现 Solution class:

# Solution(int[] nums) 使用整数数组 nums 初始化对象
# int[] reset() 重设数组到它的初始状态并返回
# int[] shuffle() 返回数组随机打乱后的结果

# 这道题主要是 洗牌问题， 如果建立一个order list 然后 遍历， 每次随机选一个数， 删除 放入新数组， 是时间复杂度是n^2
# 所以推荐 Knuth 洗牌法：
# 算法步骤为：
#                  1. 建立一个数组大小为 n 的数组 arr，分别存放 1 到 n 的数值；
#                  2. 生成一个从 0 到 n - 1 的随机数 x；
#                  3. 输出 arr 下标为 x 的数值，即为第一个随机数；
#                  4. 将 arr 的尾元素和下标为 x 的元素互换；
#                  5. 同2，生成一个从 0 到 n - 2 的随机数 x；
#                  6. 输出 arr 下标为 x 的数值，为第二个随机数；
#                  7. 将 arr 的倒数第二个元素和下标为 x 的元素互换；
#                     ...
# 时间复杂度， 空间复杂度都为O(n)
import copy
from random import randrange
from typing import List
class Solution:

    def __init__(self, nums: List[int]):

        self.nums = nums

    def reset(self) -> List[int]:
        
        return self.nums

    def shuffle(self) -> List[int]:
        # nums = copy.deepcopy(self.nums)
        # 能用list(self.nums) 尽量不用 deepcopy
        #deepcopy线性的， 如果数据量大， 用时很长
        nums = list(self.nums)
        length = len(nums)
        for i in range(length):
            r = randrange(i,length,1)
            nums[i],nums[r] = nums[r], nums[i]
        return nums
# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3]
obj = Solution(nums)
param_3 = obj.shuffle()
print(param_3)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)