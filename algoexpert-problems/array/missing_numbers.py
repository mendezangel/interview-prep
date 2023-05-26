# You're given an unordered list of unique integers nums in the range [1, n],
# where n represents the length of nums + 2. This means that two numbers
# in this range are missing from the list.

# Write a function that takes in this list and returns a new list
# with the two missing numbers, sorted numerically

# approach idea
# sort list, then count up, checking that current element is
# equal to previous num + 1. What if list[0] >, and onnly 1 num was missing in interior of list?
# would second num be placed at beginning or end?
# going to try this approach, pseudo
# sort the list
# use for loop starting at beginning + 1
# for each element, check if it is equal to previous + 1
# if yes, continue
# if no, check if equal to previous + 2, if yes add num to a list that will be returned.

# def missing_numbers(nums):
#     nums.sort()
#     final_list = []
#     for i in range(1, len(nums)):
#         current_num = nums[i]
#         previous_num = nums[i - 1]
#         if current_num == previous_num + 1:
#             continue
#         elif current_num == previous_num + 2:
#             final_list.append(current_num - 1)
#         else:
#             return [previous_num + 1, previous_num + 2]
        
    
#     return sorted(final_list)

# approach from video
# add all original numbers into a set
# for loop in range(1, len(array) + 2)
# if num in set, continue
# if it's not, add it to final array
def missing_numbers(nums):
    existing_nums = set(nums)
    final_nums = []
    for num in range(1, len(nums) + 3):
        if num not in existing_nums:
            final_nums.append(num)
    return final_nums

print(missing_numbers([1, 4, 3])) # [2, 5]
# this solution works!