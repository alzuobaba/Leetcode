#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->2>1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        rhead = None
        flag = True
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        if fast:
            rhead = slow.next
        else:
            rhead = slow

        rhead = self.reverseList(rhead)
        while head and rhead:
            flag &= (rhead.val == head.val)
            rhead = rhead.next
            head = head.next
        return flag

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


