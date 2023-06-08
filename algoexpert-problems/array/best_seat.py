# You walk into a theatre you're about to see a show in. The usher within
# the theatre walks you to your row and mentions you're allowed to sit
# anywhere within the given row. Naturally you'd like to sit in the 
# seat that gives you the most space. You also would prefer this space
# to be evenly distributed on either side of you (e.g. if there are
# three empty seats in a row, you would prefer to sit in the middle
# of those three seats).

# Given the theatre row represented as an integer array, return the seat
# index of where you should sit. Ones represent occupied sieats and
# zeroes represent empt seats.

# You may assume that someone is always sitting in the first and last
# seat of the row. Whenever there are two equally good seats, you should
# sit in the seat with the lower index. If there is no seat to sit in,
# return -1. The given array will always have a length of at least one
# and contain only ones and zeroes.

def best_seat(seats):
    i = 1
    longest_zero_length = 0
    best_seat_index = -1
    while i < len(seats):
        occupied = True if seats[i] == 1 else False
        if not occupied:
            count = 1
            j = i + 1
            while seats[j] == 0:
                count += 1
                j += 1
            if count > longest_zero_length:
                longest_zero_length = count
                best_seat_index = (i + j) // 2
            i = j + 1
        else:
            i += 1
    return best_seat_index

print(best_seat([1, 0, 1, 0, 0, 0, 1])) # 4