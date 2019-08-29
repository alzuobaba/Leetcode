# #coding:utf-8
# """
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# """
#
#
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         x = str(x)
#         if x[0] is '-':
#             x =  '-' + self.reverseString(x[1::])
#             if int(x) < -2**31:
#                 return 0
#         else:
#             x = self.reverseString(x)
#             if int(x) > 2**31-1:
#                 return 0
#         return int(x)
#
#
#     def reverseString(self, s):
#         """
#         :type s: List[str]
#         :rtype: None Do not return anything, modify s in-place instead.
#         """
#         s = [i for i in s ]
#         lenth = len(s)
#         for i in range(lenth//2):
#             s[i], s[lenth-1-i] = s[lenth-1-i], s[i]
#         return ''.join(s)
#
# print  Solution().reverse(123)
# ------------
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x[0] is '-':
            x = '-' + x[1::][::-1]
            if int(x) < -2**31:
                return 0
        else:
            x = x[::-1]
            if int(x) > 2**31-1:
                return 0
        return int(x)
print  Solution().reverse(-123)

