def right_products(array):
    for i in reversed(range(len(array) - 1)):
        current_num = array[i]
        right_num = array[i + 1]
        print(f'i: {i}')
        print(f'current num: {current_num}')
        print(f'right num: {right_num}')
        array[i] = current_num * right_num
    return array
    
print(right_products([5, 1, 4, 2])) # [40, 8, 8, 2]