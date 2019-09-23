#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        next_node = last_node = None
        while(current):
            next_node = current.next
            current.next = last_node
            last_node = current
            if next_node:
                current = next_node
            else:
                return current


m = [ListNode(i) for i in [1,2,3,4,5]]

for i in range(4):
    m[i].next = m[i+1]
m[4].next = None

Solution().reverseList(m[0])
print m