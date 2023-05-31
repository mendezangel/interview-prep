# creating a function for insertion  
def insertion_sort(array):  
    # Outer loop to traverse through 1 to len(array)
    for i in range(1, len(array)):
        print(f"\ncurrently on iteration {i}, list: {array}")

        current_num = array[i]  

        # Move elements of array[0..i-1], that are  
        # greater than current_num, to one position ahead  
        # of their current position  
        j = i - 1  
        while j >= 0 and current_num < array[j]:
            # print(f"inside while loop, list[j + 1]: {array[j + 1]}\nlist[j]: {array[j]}\nlist: {array}\nj: {j}\ni: {i}")
            array[j + 1] = array[j]
            # print(f"list after swap: {array}")
            j -= 1  
        array[j + 1] = current_num
        # print(f"finished iteration {i}, list: {array}")
    return array  
    
# Driver code to test above    
array = [10, 5, 13, 8, 2]  
print("The unsorted list is:", array)  
  
print("The sorted array is:", insertion_sort(array))