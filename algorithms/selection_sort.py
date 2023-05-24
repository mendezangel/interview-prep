# Selection sort sorts by looking for the smallest value in the list, and removing it. It repeats this until the list is empty. (this is in place, out of place would be slightly different.)
def selection_sort(arr):
    new_arr = []
    while len(arr):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        current_value = arr[i]
        if current_value < smallest:
            smallest = current_value
            smallest_index = i
    return smallest_index

print(selection_sort([3, 1, 2, 5, 4]))