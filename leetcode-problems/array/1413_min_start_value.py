# Given an array of integers nums, you start with an initial positive value, startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right)
# Return the minimum positive value of startValue such that the step by
# step sum is never less than 1.

class Solution:
    def min_start_value(self, nums: list[int]) -> int:
        negatives = 0
        for num in nums:
            if num < 0:
                negatives += num
        return abs(negatives) + 1

solution = Solution()
print(solution.min_start_value([-3, 2, -3, 4, 2])) # 5
print(solution.min_start_value([1, 2])) # 1
print(solution.min_start_value([1, -2, -3])) # 5