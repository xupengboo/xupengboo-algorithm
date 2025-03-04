# Definition for singly-linked list.
from typing import Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def addTwoNumbers(self, l1, l2, carry=0):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if l1 is None and l2 is None:
            return ListNode(carry) if carry else None  # 进位处理
        
        if l1 is None:  
            l1, l2 = l2, l1  # 确保 l1 不为空

        # ✅ 修正 s 的计算方式
        s = carry + l1.val + (l2.val if l2 else 0)
        
        l1.val = s % 10  # 当前节点值
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, s // 10)  # 递归处理下一位

        return l1


            

                    


        
        

        # 2. 两数相加 进1原则   (a + b) / 10 


        



        