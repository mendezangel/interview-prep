# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Brute force approach
# nested for loops
# Time: O(n^2)

# more optimal
# use a set
# iterate over array once,
# add each number to set
# if encounter a number already in set
# return false
# else if loop exits, return true

# Time: O(n)
# Space: O(n)
class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False

instance = Solution()
print(instance.contains_duplicate([1, 2, 3, 1])) # true
print(instance.contains_duplicate([1, 2, 3, 4])) # false
print(instance.contains_duplicate([1,1,1,3,3,4,3,2,4,2])) # true