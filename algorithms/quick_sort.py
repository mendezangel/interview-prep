# Quicksort is a recursive algorithm that uses divide and conquer.
# So you want to break down this array until you're at the base case.
# Here's how quicksort works. First, pick an element from the array. This element is called the pivot.
# For now, let's say the first item in the array is the pivot.
# Now find the elements smaller than the pivot and the elements larger than the pivot.
# this is called partitioning.
# Now you have:
# * a sub-array of all the numbers less than the pivot
# * the pivot
# * a sub array of all the numbers greater than the pivot
# The sub arrays aren't sorted. They're just partitioned. But if they were sorted,
# then sorting the whole array would be pretty easy.
# if the sub arrays are sorted, then you can combine the whole thing like this:
# left array + pivot + right array, and you get a sorted array.
# ex: [10, 15] + [33] + [] = [10, 15, 33]

# How do you sort the sub arrays? Well, the quicksort base case already knows how to sort arrays of two elements
# (the left sub array) and empty arrays (the right sub array). So if you call quicksort on the two sub arrays
# and then combine the results, you get a sorted array.

def quicksort(array):
    if len(array) < 2:
        return array # Base case: arrays with 0 or 1 element are already "sorted"
    else:
        pivot = array[0] # Recursive case
        less = [i for i in array[1:] if i <= pivot] # sub array of all the elements less than the pivot

        greater = [i for i in array[1:] if i > pivot] # sub array of all the elements greater than the pivot

        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([10, 5, 2, 3]))

# Time complexity
# Quicksort is a tricky case. In the worst case, quicksort takes O(n^2) time.
# In the average case, quicksort takes O(n log n) time.