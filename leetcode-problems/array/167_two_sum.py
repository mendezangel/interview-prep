# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# Approach
# Two Pointers
# one will point to beginning of array
# other will point to end of array
# compare the sum of the values of both pointers
# there will be three possible cases
# case 1: sum is equal to target
#   return indices of both pointers
# case 2: sum is less than target
#   increment left pointer and continue
# case 3: sum is greater than target
#   decrement right pointer and continue

# Time: O(n)
# Space: O(1)
class Solution:
    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return [start + 1, end + 1]
            elif sum < target:
                start += 1
            else:
                end -= 1
        return -1

solution = Solution()
print(solution.two_sum([2, 7, 11, 15], 9)) # [1, 2]
print(solution.two_sum([2, 3 ,4], 6)) # [1, 3]
print(solution.two_sum([-1, 0], -1)) # [1, 2]