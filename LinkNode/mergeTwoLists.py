#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = current = ListNode(0)
        m = l1
        n = l2
        while (m and n):
            if m.val < n.val:
                current.next = m
                m = m.next
            else:
                current.next = n
                n = n.next
            current = current.next

        if m:
            current.next = m
        else:
            current.next = n



