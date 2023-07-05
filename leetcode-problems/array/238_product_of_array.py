# Given an integer array nums, return an array answer such that answer[i] is equal to the product of
# all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32 bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Approach
# Create two arrays, one will hold products of nums while moving left
# other will hold products of nums while moving right
# then iterate over nums, and multiply the product of nums to the right, and left
# of where i currently is.

# Time: O(n)
# Space: O(n)
class Solution:
    # def product_except_self(self, nums: list[int]) -> list[int]:
        # products = []
        # left_products = list(nums)
        # right_products = list(nums)
        # #populate left products array
        # for i in range(1, len(left_products)):
        #     current_num = left_products[i]
        #     previous_num = left_products[i - 1]
        #     left_products[i] = current_num * previous_num
        # # populate right products array
        # for i in range(len(nums) - 2, -1, -1):
        #     current_num = nums[i]
        #     previous_num = right_products[i + 1]
        #     right_products[i] = current_num * previous_num
        # # populate products
        # for i, num in enumerate(nums):
        #     left_product = left_products[i - 1] if i > 0 else 1
        #     right_product = right_products[i + 1] if i < len(nums) - 1 else 1
        #     products.append(left_product * right_product)
        # return products

# Optimal solution
# Time: O(n)
# Space: O(1)
    def product_except_self(self, nums: list[int]) -> list[int]:
        products = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            products[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= postfix
            postfix *= nums[i]
        return products
        


solution = Solution()
print(solution.product_except_self([1, 2, 3, 4])) # [24, 12, 8, 6]
print(solution.product_except_self([-1, 1, 0, -3, 3])) # [0, 0, 9, 0, 0]