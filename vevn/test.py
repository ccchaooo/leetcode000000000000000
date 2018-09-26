class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        for i, x in enumerate(self.nums):
            for j, y in enumerate(self.nums):
                if x + y == self.target and i != j:
                    ret = [i, j]
                    return ret
        return 0

li = [3,2,4]
So = Solution()
print(So.twoSum(li,5))