# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', 'u', and they can appear in both lower and upper cases, more than once.

# Constraints
# 1 <= s.length <= 3 * 10^5
# s consits of printable ASCII characters

# Reasoning
# like reversing a string but only reversing the vowels
# so all non vowel chars should still retain original position

# Approach - Two Pointer
# convert string to char array
# where i will be looking at start of array, and j will be looking at end
# use while loop, while i < j
# move pointers until they are both looking at a vowel
# swap their places, and inc/dec pointers
# once loop exits, convert array to string and return

# Time: O(n)
# Space: O(n) where n is length of input string

class Solution:
    def reverse_vowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        array = [*s]
        i = 0
        j = len(array) - 1
        while i < j:
            start_char = array[i].lower()
            end_char = array[j].lower()
            if start_char not in vowels:
                i += 1
            elif end_char not in vowels:
                j -= 1
            else:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        return ''.join(array)

solution = Solution()
print(solution.reverse_vowels('hello')) # 'holle'
print(solution.reverse_vowels('leetcode')) # 'leotcede'