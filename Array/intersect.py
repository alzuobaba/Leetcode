class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
# 1.---------------- n2 time , n space
#         ret = []
#         for i in nums1:
#             if i in nums2:
#                 ret.append(i)
#
#         return ret

# 2.-----------------
# also sorted
        nums1.sort()
        nums2.sort()
        ret = []
        g1 = (x for x in nums1)
        g2 = (x for x in nums2)
        try:
            m = next(g1)
            n = next(g2)
        except:
            return ret
        while True:
            try:
                if m == n:
                    ret.append(m)
                    m = next(g1)
                    n = next(g2)
                elif m>n:
                    n = next(g2)
                else:
                    m = next(g1)
            except:
                return ret









print Solution().intersect([1,2,2,4,6],[2,2,5])