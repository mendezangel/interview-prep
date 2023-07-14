def minStart(arr):
    min_starting_val = 1 - arr[0] if 1 - arr[0] > 0 else 1
    for num in arr:
        print(f'min starting val: {min_starting_val}')
        sum = num + min_starting_val
        print(f'current num: {num}')
        print(f'sum: {sum}')
        if sum < 1:
            min_starting_val += 1 - sum
    return min_starting_val
    
print(minStart([10, -5, 4, -2, 3, 1, -1, -6, -1, 0, 5]))