# Given a signed 32-bit integer x, return x with its digits reversed.
# if reversing x causes the value to go outside the 32-bit integer range [-2^31, 3^31 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        string = '-' + string[:0:-1] if x < 0 else string[::-1]
        new_int = int(string)
        if new_int < -2**31 or new_int > 2**31 - 1:
            new_int = 0
        return new_int

solution = Solution()
print(solution.reverse(123)) # 321
print(solution.reverse(-123)) # -321
print(solution.reverse(120)) # 21
print(solution.reverse(1534236469)) # 0

# the obvious solution here is to convert the int into a string, reverse the string, convert string back into an int, and return new int.
# problems?
# negative sign (-) needs to stay in front, 123-

# approach
# initialize a string variable, converting x into a string
# depending on if x < 0 or not, reversal process will differ
# convert string back to int, return