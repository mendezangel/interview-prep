# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# Time: O(n)
# Space: O(n)
class Solution:
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums: # adding each num to dictionary, with num of appearances as it's value
            count[num] = 1 + count.get(num, 0)
        
        for n, c in count.items(): # populating the bucket
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # iterating bucket, starting from the end
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
    
solution = Solution()
print(solution.top_k_frequent([1, 1, 1, 2, 2, 3], 2)) # [1, 2]
print(solution.top_k_frequent([1], 1)) # [1]
print(solution.top_k_frequent([1, 2], 2)) # [1, 2]