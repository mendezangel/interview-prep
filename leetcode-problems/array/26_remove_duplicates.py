# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in place such that each unique element
# appears only once. The relative order of the elements should be
# kept the same. Then return the number of unique elements in nums.

# consider the number of unique elements of nums to be k,
# to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums
# contain the unique elements in the order they were present in
# nums initially. The remaining elements of nums are not important
# as well as the size of nums.
# return k.

# Time: O(n)
# Space: O(1)

class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            current_num = nums[i]
            if i < len(nums) - 1 and current_num == nums[i + 1]:
                nums.pop(i + 1)
                continue
            i += 1
        return len(nums)

solution = Solution()
print(solution.remove_duplicates([1, 1, 2])) # 2
print(solution.remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])) # 5