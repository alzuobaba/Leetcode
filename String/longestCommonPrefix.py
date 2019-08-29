#coding:utf-8
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs and strs[0]:
            min_lenth = len(strs[0])
        else:
            return ''
        for i in strs:
            if len(i) < min_lenth:
                min_lenth = len(i)
        # if min_lenth ==0:
        for i in range(min_lenth):
            for str_s in strs[1:]:
                if strs[0][i]==str_s[i]:
                    continue
                else:
                    return strs[0][:i]

        return strs[0][:min_lenth]

print Solution().longestCommonPrefix(["f",''])