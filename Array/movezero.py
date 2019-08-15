class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # dp
        i = j = 0
        lenth = len(nums)
        while j < lenth:
            if nums[j] == 0:
                j += 1
                continue
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        while i < lenth:
            nums[i] = 0
            i += 1
        return nums

print Solution().moveZeroes([0,3,2,0,2,3])