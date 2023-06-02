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

def smallest_difference(arrayOne, arrayTwo):
    smallest_num = float('inf')
    nums = []
    for first_num in arrayOne:
        for second_num in arrayTwo:
            diff = abs(first_num - second_num)
            if diff < smallest_num:
                smallest_num = diff
                nums = [first_num, second_num]
    return nums

print(smallest_difference([-1,5, 10, 20, 28, 3], [26, 134, 135, 15, 17])) # [28, 26]