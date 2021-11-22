class Solution:
  ## Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
  # Example
  #
  # Input: nums = [1, 2, 3, 4]
  # Output: 24


  ## 解题思路: 三个数的乘积, 如果brute force 则 时间复杂度为 O(n^3), for 中套 for, 太麻烦了

  def maximumProduct(self, nums: List[int]) -> int:

