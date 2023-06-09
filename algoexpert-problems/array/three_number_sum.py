# Write a function that takes in a non empty array of distinct integers
# and an integer representing a target sum. The function should find
# all triplets in the array that sum up to the target sum and return a 
# two dimensional array of all these triplets. The numbers in each
# triplet should be ordered in ascending, order, and the triplets
# themselves should be ordered in ascending order with respect to the
# numbers they hold.

# If no three numbers sum upto the target sum, the function should return
# an empty array

# Time: O(n^2) Space: O(n)
def three_number_sum(array, targetSum):
    sorted_array = sorted(list(array))
    sums = []
    for i, num in enumerate(sorted_array):
        two_sum_target = targetSum - num
        dict = {}
        for j in range(i + 1, len(sorted_array)):
            current_num = sorted_array[j]
            difference = two_sum_target - current_num
            if difference in dict:
                sums.append([num, difference, current_num])
            dict[current_num] = j
    return sums

print(three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)) # [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]