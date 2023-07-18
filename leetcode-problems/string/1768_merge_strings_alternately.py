# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# word1 = abc, word2 = pqr
# new string, add a
# add p -> ap
# add b -> apb
# add q -> apbq
# add c -> apbqc
# add r -> apbqcr
# return new string

# Approach
# two pointers
# declare empty list
# while loop, while both pointers are less than their respective word lengths
# once loop exits, join list to string, and return

# Time: O(n + m) where n is length of word1, and m is length of word2
# Space: O(n + m) where n is length of word1, and m is length of word2

class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        pointer_one = 0
        pointer_two = 0
        letter_list = []
        while pointer_one < len(word1) or pointer_two < len(word2):
            if pointer_one < len(word1):
                letter_list.append(word1[pointer_one])
                pointer_one += 1
            if pointer_two < len(word2):
                letter_list.append(word2[pointer_two])
                pointer_two += 1
        return ''.join(letter_list)

solution = Solution()
print(solution.merge_alternately('abc', 'pqr')) # apbqcr
print(solution.merge_alternately('ab', 'pqrs')) # apbqrs
print(solution.merge_alternately('abcd', 'pq')) # apbqcd