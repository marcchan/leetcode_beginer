# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
#
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
#
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
#
# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
# Input: s = "ab", goal = "ab"
# Output: false
#
# Input: s = "aa", goal = "aa"
# Output: true
# 方法一： 制定一个数， 然后遍历 O(n^2)
# 方法二： 线遍历 找到不同的值， 然后交换看是否相同， O(n) 空间O(n)
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        diff_list = []
        # 长度不同直接false
        if len(s) != len(goal):
            return False
        # 由于必须交换一次，在str相同的情况下，交换相同的字符
        if s == goal and len(set(s)) < len(goal): return True
        # 除此之外 去不同， 观察
        for index in range(len(s)):
            if s[index] != goal[index]:
                diff_list.append(index)
        return len(diff_list) ==2 and \
               s[diff_list[0]] == goal[diff_list[1]] and \
               s[diff_list[1]] == goal[diff_list[0]]




s = "aa"
goal = "aa"
so = Solution()
print(so.buddyStrings(s,goal))