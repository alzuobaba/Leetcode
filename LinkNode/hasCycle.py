#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while True:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

