# v1.0 简单的通过列表实现
class Queue:

    def __init__(self):
        self.queue = []
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        temp = self.queue[len(self.queue) - 1]
        self.queue.remove(temp)
        return  temp
    
    # 时间复杂度：O(n) 不适用
    def enqueue(self, value):
        self.queue.insert(0, value)

    def view(self):
        for _ in self.queue:
            print(_)

q = Queue()
# 1. 入队操作
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.view()
# 5. 清空队列
q.dequeue()
q.view()


# # v2.0 通过将列表中的insert替换成 popleft 和 append 降低时间复杂度。
# from collections import deque

# class Queue:
    
#     def __init__(self):
#         self.queue = deque()
    
#     def consumer(self):
#         if len(self.queue) == 0:
#             return None
#         return self.queue.popleft()  # 从队头移除元素
    
#     def producer(self, value):
#         self.queue.append(value)  # 向队尾添加元素


# # v3.0 还可以基于链表实现
# class Node:
#     """链表节点类"""
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Queue:
#     """队列实现（基于链表）"""
#     def __init__(self):
#         self.head = None  # 队首节点
#         self.tail = None  # 队尾节点
#         self._size = 0    # 队列长度

#     def enqueue(self, value):
#         """入队操作：将元素添加到队尾"""
#         new_node = Node(value)
#         if self.tail is None:
#             # 队列为空时，头尾均指向新节点
#             self.head = self.tail = new_node
#         else:
#             # 非空队列：将新节点链接到队尾，并更新队尾指针
#             self.tail.next = new_node
#             self.tail = new_node
#         self._size += 1

#     def dequeue(self):
#         """出队操作：移除并返回队首元素"""
#         if self.is_empty():
#             raise IndexError("Dequeue from empty queue")
        
#         # 保存队首节点的值，并更新头指针
#         value = self.head.value
#         self.head = self.head.next
#         self._size -= 1
        
#         # 如果出队后队列为空，更新尾指针
#         if self.head is None:
#             self.tail = None
#         return value

#     def peek(self):
#         """查看队首元素（不删除）"""
#         if self.is_empty():
#             raise IndexError("Peek from empty queue")
#         return self.head.value

#     def is_empty(self):
#         """判断队列是否为空"""
#         return self._size == 0

#     def __len__(self):
#         """返回队列长度"""
#         return self._size

#     def __str__(self):
#         """可视化队列内容（调试用）"""
#         values = []
#         current = self.head
#         while current:
#             values.append(str(current.value))
#             current = current.next
#         return " -> ".join(values) if values else "Empty Queue"