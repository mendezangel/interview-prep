# For two string s and t, we say "t divides s" if and only if
# s = t + ... + t (i.e., t is concatenated with itself one
# or more times).

# Given two string str1 and str2, return the largest string x such
# that x divides both str1 and str2

# brute force
# find the shorter string among str1 and str2
# start with base = shorter string, and check if both str1 and str2 are made of multiples of base.
#   if so, return base.
#   otherwise, we shall try a shorter string by removing the last character from base.
# if we have checked all prefix strings without finding the gcd string, return ''

class Solution:
    pass

solution = Solution()
print(solution.gcd_of_strings('ABCABC', 'ABC')) # 'ABC'
print(solution.gcd_of_strings('ABABAB', 'ABAB')) # 'AB'
print(solution.gcd_of_strings('LEET', 'CODE')) # ''