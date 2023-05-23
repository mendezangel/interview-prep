# Write a function, intersection, that takes in two lists, a, b,
# as arguments. The function should return a new list containing
# elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate
# elements.

def intersection(a, b):
    nums = {}
    final_list = []
    for i, num in enumerate(a):
        if num not in nums:
            nums[num] = i

    for num in b:
        if num in nums:
            final_list.append(num)
    return final_list

print(intersection([4,2,1,6], [3,6,9,2,10])) # -> [2,6]
print(intersection([2,4,6], [4,2])) # -> [2,4]
print(intersection([4,2,1], [1,2,4,6])) # -> [1,2,4]
print(intersection([0,1,2], [10,11])) # -> []
a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
# print(intersection(a, b)) # -> [0,1,2,3,..., 49999]