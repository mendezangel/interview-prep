# a phrase is a palindrome if, after converting all uppercase letters into lowercase
# letters and removing all non-alphanumeric characters, it reads the same forward
# and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Approach
# two pointers
# one pointer will be at start of string
# other at end
# compare character both pointers are looking at, if equal continue, else return false
# pointers will ignore non alphanumeric characters, so if pointing at a non
# alphanumeric character, move pointer to next character

# Time: O(n)
# Space: O(n)
class Solution:
    # suboptimal
    # def is_palindrome(self, s: str) -> bool:
    #     newStr = ''
    #     for c in s:
    #         if c.isalnum():
    #             newStr += c.lower()
    #     return newStr == newStr[::-1]
    
    # optimal, constant space
    def is_palindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start <= end:
            start_character = s[start].lower()
            end_character = s[end].lower()
            if not start_character.isalnum():
                start += 1
                continue
            if not end_character.isalnum():
                end -= 1
                continue
            if start_character != end_character:
                return False
            start += 1
            end -= 1
        return True

instance = Solution()
print(instance.is_palindrome("A man, a plan, a canal: Panama")) # True
print(instance.is_palindrome("race a car")) # false
print(instance.is_palindrome(" ")) # true