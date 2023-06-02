# Write a function that takes in two non empty arrays of integers,
# finds the pair of numbers (one from each array) whose absolute difference
# is closest to zero, and returns an array containing these two
# numbers, with the number from the first array in the first position.

# Note that the absolute difference of two integers is the distance
# between them on the real number line. For example, the absolute difference
# between -5 and 5 is 10, and the absolute difference of -5 and -4
# is 1.

# You can assume that there will only be one pair of 
# numbers with the smallest difference

# def smallest_difference(arrayOne, arrayTwo):
#     smallest_num = float('inf')
#     nums = []
#     for first_num in arrayOne:
#         for second_num in arrayTwo:
#             diff = abs(first_num - second_num)
#             if diff < smallest_num:
#                 smallest_num = diff
#                 nums = [first_num, second_num]
#     return nums

def smallest_difference(arrayOne, arrayTwo):
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    smallest_num = float('inf')
    nums = []
    i = 0
    j = 0
    while i < len(arrayOne) and j < len(arrayTwo):
        num_one = arrayOne[i]
        num_two = arrayTwo[j]
        if num_one == num_two:
            return [num_one, num_two]
        diff = abs(num_one - num_two)
        if diff < smallest_num:
            smallest_num = diff
            nums = [num_one, num_two]
        if num_one < num_two:
            i += 1
        else:
            j += 1
    return nums

print(smallest_difference([-1,5, 10, 20, 28, 3], [26, 134, 135, 15, 17])) # [28, 26]