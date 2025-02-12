class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 创建链表 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

node = head.next
new_node = ListNode(4)
new_node = node.next
node.next = new_node


node.next = node.next.next


