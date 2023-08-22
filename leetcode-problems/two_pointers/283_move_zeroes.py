# Given an integer array nums, move all 0's to the end of it while maintaining the relative order
# of all non zero elements.

# Note that you must do this all in place without making a copy of the array.

# Example 1:
# Input: nums = [0, 1, 0, 3, 12]
# Ouput: [1, 3, 12, 0, 0]

# Example 2:
# Input: [0]
# Output: [0]

class Solution:
    def move_zeroes(self, nums: list[int]) -> None:
        i = 0
        while i < len(nums):
            current_num = nums[i]
            if current_num == 0:
                nums.append(current_num)
                nums.pop(i)
                continue
            i += 1

solution = Solution()
print(solution.move_zeroes([0, 1, 0, 3, 12])) # [1, 3, 12, 0, 0]
print(solution.move_zeroes([0])) [0]