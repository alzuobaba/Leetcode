class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        lenth = len(nums)
        if lenth == i:
            return i
        for j in range(lenth):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i+1

class Solution_official(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <=1:
            return len(nums)
        index = 0
        i = 0
        while i < len(nums):
            if nums[index] != nums[i]:
                index+=1
                nums[index] = nums[i]
            i+=1

        return index+1
