

# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        seconds =0
        for i in range(k):
            seconds += self._rotate(nums,i,k)
            print 'dddd---',seconds
            if seconds ==len(nums):
                break
        return nums


    def _rotate(self, nums, i,k):
        seconds = 0
        rk =i
        lenth = len(nums)
        tmp = nums[i]
        while True:

            # rk = self.r_key(len(nums),k,rk)
            rk =(rk+k)%lenth
            value = nums[rk]
            nums[rk] = tmp
            seconds += 1
            print rk,seconds

            if seconds == len(nums):
                return seconds
            tmp = value

            if rk == i:
                return seconds

    @staticmethod
    def r_key(lenth, k, index):
        if k + index + 1 > lenth:
            the_right = (k + index) % lenth
        else:
            the_right = k + index
        return the_right


nums = [1, 2, 3, 4, 5,6,7]
k = 3
print Solution().rotate(nums, k)




# print  Solution().rotate([1,2,3,4,5,6,7],3)
# print Solution.r_key(7,6,3)

a = [1,2,3,4,5]
print id(a)
print id(a[1:])