# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# an anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# sub optimal approach
# sort both strings
# return string1 == string2
# Time: O(nlogn)
# Space: O(1)

# optimal approach
# use a dictionary

# Time: O(n)
# Space: O(n)
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictS, dictT = {}, {}
        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)
        return dictS == dictT        

instance = Solution()
print(instance.is_anagram("anagram", "nagaram")) # true
print(instance.is_anagram("rat", "car")) # false