class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        dictionary = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in dictionary:
                return [dictionary[difference], i]
            dictionary[num] = i
        return -1
    
instance = Solution()
print(instance.two_sum([2, 7, 11, 15], 9)) # [0, 1]