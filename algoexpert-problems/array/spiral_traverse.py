# Write a function that takes an n x m two-d array (that can be square
# shaped when n==m) and returns a one-dimensional array of all the 
# array's elements in spiral order.

# spiral order starts at the top left corner of the two D array, goes
# to the right, and proceeds in a spiral pattern all the way until
# every element has been visited

# this is basically just printing all the values in a matrix with a slight twist

def spiral_traverse(array):
    spiral_list = []
    queue = [[0, 0]]
    visited = set()
    while len(queue):
        location = queue.pop(0)
        row = location[0]
        column = location[1]
        visited.add(f'({row}, {column})')
        spiral_list.append(array[row][column])
        available_neighbor = find_available_neighbor(array, visited, row, column)
        if available_neighbor is not None:
            queue.append(available_neighbor)
    return spiral_list

def find_available_neighbor(matrix, visited, row, column):
    position = None
    # check right
    if column + 1 < len(matrix[row]) and f'({row}, {column + 1})' not in visited:
        position = [row, column + 1]
        visited.add(f'({row}, {column + 1})')
    # check bottom
    elif row + 1 < len(matrix) and f'({row + 1}, {column})' not in visited:
        position = [row + 1, column]
        visited.add(f'({row + 1}, {column})')
    # check left
    elif column - 1 >= 0 and f'({row}, {column - 1})' not in visited:
        position = [row, column - 1]
        visited.add(f'({row}, {column - 1})')
    # check top
    elif row - 1 >= 0 and f'({row - 1}, {column})' not in visited:
        position = [row - 1, column]
        visited.add(f'({row - 1}, {column})')

    return position

array = [
    [1,  2,  3,  4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7]
]

print(spiral_traverse(array)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]