#coding:utf-8
"""
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。



示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def convert(input_str):
            string = ""
            index = 1
            for i in range(len(input_str)):
                if i == len(input_str)-1:
                    string += str(index) + input_str[i]
                    break
                if input_str[i] != input_str[i+1]:
                    string += str(index) + input_str[i]
                    index = 1
                else:
                    index += 1
            return string

        input_str = '1'
        for i in range(n-1):
            input_str = convert(input_str)
        return input_str

print Solution().countAndSay(4)