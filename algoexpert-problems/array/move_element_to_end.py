# You're given an array of integers and an integer. Write a function
# that moves all instances of that integer in the array to the end of the
# array and returns the array.

# The function should perform this in place (i.e it should mutate the input array) and doesn't need to maintain the order of the other integers

def move_element_to_end(array, toMove):
    left = 0
    right = len(array) - 1
    while left < right:
        # print(f'\nArray at start: {array}')
        # print(f'left value: {left}')
        # print(f'right value: {right}')
        if array[right] == toMove:
            right -= 1
        elif array[left] == toMove:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        else:
            left += 1
        # print(f'array at end: {array}')
        # print(f'left at end: {left}')
        # print(f'right at end: {right}')
    return array

print(move_element_to_end([2, 4, 2, 5, 6, 2, 2], 2)) # [1, 3, 4, 2, 2, 2, 2, 2] the numbers 1, 3, and 4 could be ordered differently