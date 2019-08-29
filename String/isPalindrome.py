#coding:utf-8
"""
“回文串”是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串。

验证回文字符串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([i.lower() for i in s if i.isalnum()])
        if s == s[::-1]:
            return True
        return False

Solution().isPalindrome('12f43;,.dde#$$@3ff&')