# You're given an unordered list of unique integers nums in the range [1, n],
# where n represents the length of nums + 2. This means that two numbers
# in this range are missing from the list.

# Write a function that takes in this list and returns a new list
# with the two missing numbers, sorted numerically

def missing_numbers(nums):
    nums.sort()
    final_list = []
    for i in range(1, len(nums)):
        current_num = nums[i]
        previous_num = nums[i - 1]
        if current_num == previous_num + 1:
            continue
        elif current_num == previous_num + 2:
            final_list.append(current_num - 1)
        else:
            return [previous_num + 1, previous_num + 2]
    return sorted(final_list)

print(missing_numbers([1, 4, 3])) # [2, 5]