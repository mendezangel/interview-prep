# Write a function that takes in a non empty array of integers and returns an array of the same length,
# Where each element in the output array is equal to the product of ever other number in the input array.

# In other words, the value at output[i] isequal to the product of every number in the input array other than input[i]

# Note that you're expected to solve this problem without using division

def arrayOfProducts(array):
    product_array = []
    for i, num_i in enumerate(array):
        product = 1
        for j, num_j in enumerate(array):
            if i == j:
                continue
            product *= num_j
        product_array.append(product)
    return product_array

print(arrayOfProducts([5, 1, 4, 2])) # [8, 40, 10, 20]