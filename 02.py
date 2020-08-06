#-*- codeing=utf-8 -*-
#@time: 2020/8/6 22:34
#@Author: Shang-gang Lee

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        curr = head
        carry = 0
        while carry or l1  or l2:
            sum = carry
            sum +=(l1.val if l1 else 0) +(l2.val if l2 else 0)
            curr.next = ListNode(sum % 10)
            curr = curr.next
            carry = sum // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
