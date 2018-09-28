# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def addTwoNumbers(self, l1, l2):
        # 链表长度
        # 总数
        sum = 0

        ret,ent = self.sum2(l1.val, l2.val)

        sum = ret

        return

    def sum2 (self, x, y):
        return ( x + y ) % 10, x + y >= 10

#
# l1=[2,4,3]
# l2=[5,6,4]
# so = Solution()
# so.addTwoNumbers(l1,l2)
