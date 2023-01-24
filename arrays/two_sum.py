# Problem Statement
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Eg:nums [2,7,11,15] target = 9
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        _dict = {}
        for each in nums:
            _dict[each] = index
        
        nums_sort = nums.sort()

        







if __name__ == "__main__":
    sol = Solution()
    n = 315
    ans = sol.isUgly(-2147483648)
    print("answer", ans)