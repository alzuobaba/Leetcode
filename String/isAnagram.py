#coding:utf-8
"""
两个单词如果包含相同的字母，次序不同，则称为字母易位词(anagram)。
例如，“silent”和“listen”是字母易位词，而“apple”和“aplee”不是易位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def get_dict(s):
            dic = {}
            for i in s:
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] += 1
            return dic

        if len(s) != len(t):
            return False
        if get_dict(s) == get_dict(t):
            return True
        return False


s= 'dfgfd'
t= 'dsgef'
print  Solution().isAnagram(s,t)