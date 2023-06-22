# Write a function that takes in a non-empty array of intergers
# and returns an array of the same length, where each element in
# the output array is equal to the product of every other product
# of every other number in the input array.

# In other words, the value at output[i] is equal to the product of every
# number in the input array other than input[i].

# Note that you're expected to solve this problem without using division.

def array_of_products(array):
    products = []
    left_products = list(array)
    right_products = list(array)
    for i in range(1, len(left_products)):
        current_num = left_products[i]
        previous_num = left_products[i - 1]
        left_products[i] = current_num * previous_num
    for i in reversed(range(len(right_products) - 1)):
        current_num = right_products[i]
        right_num = right_products[i + 1]
        right_products[i] = current_num * right_num
    # at this point we have our left and right products
    for i in range(len(array)):
        left_product = left_products[i - 1] if i > 0 else 1
        right_product = right_products[i + 1] if i < len(right_products) - 1 else 1
        products.append(left_product * right_product)
    return products


print(array_of_products([5, 1, 4, 2])) # [8, 40, 10, 20]