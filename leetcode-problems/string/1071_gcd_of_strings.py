# For two string s and t, we say "t divides s" if and only if
# s = t + ... + t (i.e., t is concatenated with itself one
# or more times).

# Given two string str1 and str2, return the largest string x such
# that x divides both str1 and str2

# two pointers
# one pointer will look at str1, and other will look at str2
# while pointer two is less than str2 length
# compare both letters, if match keep incrementing pointers
# for each letter add it to a set

class Solution:
    def gcd_of_strings(self, str1: str, str2: str) -> str:
        pass

solution = Solution()
print(solution.gcd_of_strings('ABCABC', 'ABC')) # 'ABC'
print(solution.gcd_of_strings('ABABAB', 'ABAB')) # 'AB'
print(solution.gcd_of_strings('LEET', 'CODE')) # ''