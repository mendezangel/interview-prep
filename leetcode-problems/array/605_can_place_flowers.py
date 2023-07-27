# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
# and an integer n, return true if n new flowers can be planted in teh flowerbed without 
# violating the no adjacent flowers rule and false otherwise.

# Reasoning
# essentially all we have to do is count all the 0's with a 0 to it's left and right

# Approach
# we only need to iterate over the array once
# for each 0, check its left and right, if they are both 0, increment some var
# that will be keeping track
# compare that var to n, if equal, return true
# outside of the loop return 0

class Solution:
    def can_place_flowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        for i, num in enumerate(flowerbed):
            prev_plot = 0 if i == 0 else flowerbed[i - 1]
            next_plot = 0 if i >= len(flowerbed) - 1 else flowerbed[i + 1]
            if num == 0:
                if prev_plot == 0 and next_plot == 0:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return False

solution = Solution()
print(solution.can_place_flowers([1, 0, 0, 0, 1], 1)) # True
print(solution.can_place_flowers([1, 0, 0, 0, 1], 2)) # False
print(solution.can_place_flowers([0, 0, 1, 0, 0], 2)) # True