# you're given a list of integers nums. Write a function that returns
# a boolean representing whether there exists a zero-sum subarray of
# nums.

# a zero sum subarray is any subarray where all of the values add up 
# to zero. A subarray is any contiguous section of the array.
# For the purpose of this problem, a subarray can be as small as one
# element and as long as the original array.

# psuedo for brute force solution
# declare i equal to 0
# while loop, condition is i < array length
# declare sum variable equal to array[i]
# for loop, with j equal to i + 1
# keep adding to sum var while j increases
# if sum ever equal to 0 return True
# after for loop increment i
# return False after while loop

# def zero_sum_subarray(nums):
#     i = 0
#     while i < len(nums):
#         if nums[i] == 0:
#             return True
#         sum = nums[i]
#         for j in range(i + 1, len(nums)):
#             sum += nums[j]
#             if sum == 0:
#                 return True
#         i += 1
#     return False

# optimal solution
def zero_sum_subarray(nums):
    sum = 0
    sums = {sum}
    for num in nums:
        sum += num
        if sum in sums:
            return True
        else:
            sums.add(sum)
    return False

print(zero_sum_subarray([-5, -5, 2, 3, -2])) # True, The subarray [-5, 2, 3] has a sum of 0

# brute force: Time: O(n^2) Space: O(1)
# optimal: Time: O(n) Space: O(n)
# n for both is length of nums array