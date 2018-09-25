# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        for i, x in enumerate(self.nums):
            for j, y in enumerate(self.nums):
                if x + y == self.target:
                    return [i, j]
        return [-1, -1]


So = Solution(range(10), 5)
So.twoSum()