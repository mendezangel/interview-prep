# Write a function that takes in an array of integers and returns the length of the longest peak in the array.

# A peak is defined as adjacent integers in the array that are strictly increasing
# until they reach a tip (the highest value in the peak), at wich point they become strictly decreasing.
# At least three integers are required to form a peak.

# For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do
# the integers 1, 2, 2, 0.
# Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing 
# integers after the 3.

def longest_peak(array):
    i = 1
    longest = 0
    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not is_peak:
            i += 1
            continue

        left_index = i - 2
        right_index = i + 2
        while left_index >= 0 and array[left_index] < array[left_index + 1]:
            left_index -= 1
        while right_index < len(array) and array[right_index] < array[right_index - 1]:
            right_index += 1
        current_peak = right_index - left_index - 1
        longest = max(longest, current_peak)
        i = right_index
    return longest

print(longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])) # Output: 6, peak is 0, 10, 6, 5, -1, -3