# There are n kids with candies. You are given an integer array candies, 
# where each candies[i] represents the number of candies the ith kid has, 
# and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, 
# after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

# Approach
# declare empty array, to hold bools
# iterate over array, to find the largest number
# iterate over array again, adding extra candies to candies[i] and comparing it to the largest num
# if larger, add True to output array, otherwise, add False
# return output array

# Time: O(n + n) -> O(2n) -> O(n)
# Space: O(n)
class Solution:
    def kids_with_candies(self, candies: list[int], extraCandies: int) -> list[bool]:
        output_array = []
        highest_num = 0
        for num in candies:
            if num > highest_num:
                highest_num = num
        
        for num in candies:
            current_num = extraCandies + num
            if current_num >= highest_num:
                output_array.append(True)
            else:
                output_array.append(False)
        return output_array

solution = Solution()
print(solution.kids_with_candies([2, 3, 5, 1, 3], 3)) # [True, True, True, False, True]
print(solution.kids_with_candies([4, 2, 1, 1, 2], 1)) # [True, False, False, False, False]
print(solution.kids_with_candies([12, 1, 12], 10)) # [True, False, True]
