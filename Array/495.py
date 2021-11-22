from typing import List
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if (len(timeSeries) < 1) | (len(timeSeries) > 10*4 | duration > 10*7):
            return 0
        else:
            res: int = 0
            new_time: int = 0
            for time in timeSeries:
                if (new_time > time):
                    res = res - new_time + time + duration
                else:
                    res += duration

                new_time = time + duration

            return  res

print(10**4)

ex = Solution()
nums: List[int] = [1,2,3,4,5]
print(ex.findPoisonedDuration(timeSeries=nums,duration= 5))
