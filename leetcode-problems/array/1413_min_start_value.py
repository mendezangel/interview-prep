# Given an array of integers nums, you start with an initial positive value, startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right)
# Return the minimum positive value of startValue such that the step by
# step sum is never less than 1.


# Declare a min starting variable, and sum var initialized to min start
# instead of a for loop, use a pointer in a while?
# declare pointer
# while loop, pointer is less than nums length
# iterate over array as normal, adding each num to sum var
# with each iteration check if sum var goes below 1:
#   if not, continue
#   if yes calculate difference with sum and 1, add that difference to min start, reset pointer to 1 and sum pointer to min_start
# after while loop, return min start value

# Time: O(n)
# Space: O(1)
class Solution:
    def min_start_value(self, nums: list[int]) -> int:
        min_start = 1 if nums[0] > 0 else 1 - nums[0]
        sum = min_start
        i = 0
        while i < len(nums):
            steps += 1
            current_num = nums[i]
            sum += current_num
            if sum < 1:
                difference = 1 - sum
                min_start += difference
                sum = min_start
                i = 0
            else:
                i += 1
        return min_start

solution = Solution()
print(solution.min_start_value([-3, 2, -3, 4, 2])) # 5
print(solution.min_start_value([1, 2])) # 1
print(solution.min_start_value([1, -2, -3])) # 5
print(solution.min_start_value([-1, -2, -3, -4, -5, -6]))