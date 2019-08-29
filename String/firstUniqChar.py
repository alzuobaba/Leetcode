#coding:utf-8
"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcodev",
返回 2.


注意事项：您可以假定该字符串只包含小写字母。
"""


# class Solution(object):
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         ans = 0
#         black_index= set()
#         for i in range(len(s)):
#             if i in black_index:
#                 continue
#             ans = 0
#             for j in range(i+1, len(s)):
#                 if j in black_index:
#                     continue
#                 if s[j] == s[i]:
#                     black_index.add(j)
#                     ans += 1
#             if ans == 0:
#                 return i
#         return -1
class Solution(object):

    def firstUniqChar(self, s):
        # 先假设最小索引为最后的字符索引
        min_unique_char_index = len(s)

        # 已知字符串由小写字母构成，则遍历a-z
        for c in "abcdefghijklmnopqrstuvwxyz":
            i = s.find(c)
            # 分别从目标的字符串头和字符串尾查找对应字母的索引；如果两索引相等，则说明是单一字符
            if i != -1 and i == s.rfind(c):
                # 更新最新的最小索引
                min_unique_char_index = min(min_unique_char_index, i)

        # 如果返回值不为最后字符的索引，则返回最小索引值
        # 否则，根据题意，返回-1
        return min_unique_char_index if min_unique_char_index != len(s) else -1


print  Solution().firstUniqChar('leetlcode')