class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # lenth = len(nums)
        # for i in range(lenth):
        #     if nums.pop() in nums:
        #         return True
        # else:
        #     return False

        # nums.sort()
        # tmp = None
        # for i in nums:
        #     if i == tmp:
        #         return True
        #     else:
        #         tmp = i
        # else:
        #     return False
        return len(nums) != len(set(nums))

nums = [1,1,1,3,3,4,3,2,4,2]

print  Solution().containsDuplicate(nums)
