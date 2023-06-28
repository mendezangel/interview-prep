# given an array of strings strs, group the anagrams together. You can return the answer in any order.

# an anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# approach
# define a dictionary
# iterate over every word in array
# with each word, sort the word then do one of two things:
# if sorted word is not present in the dictionary, add it as a key, and for its value create a list and add the non sorted version of the word to it
# if sorted word is present in the dictionary, add non sorted word to that key's list
# once iteration is finished return dictionary values as an array

# Time: O(n log n)
# Space: O(n)
class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted([*word]))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
        return list(anagrams.values())

solution = Solution()
print(solution.group_anagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(solution.group_anagrams([''])) # [['']]
print(solution.group_anagrams(['a'])) # [['a']]