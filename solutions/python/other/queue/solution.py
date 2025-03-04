class Node:
    """链表节点类"""
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """队列实现（基于链表）"""
    def __init__(self):
        self.head = None  # 队首节点
        self.tail = None  # 队尾节点
        self._size = 0    # 队列长度

    def enqueue(self, value):
        """入队操作：将元素添加到队尾"""
        new_node = Node(value)
        if self.tail is None:
            # 队列为空时，头尾均指向新节点
            self.head = self.tail = new_node
        else:
            # 非空队列：将新节点链接到队尾，并更新队尾指针
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        """出队操作：移除并返回队首元素"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        
        # 保存队首节点的值，并更新头指针
        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        
        # 如果出队后队列为空，更新尾指针
        if self.head is None:
            self.tail = None
        return value

    def peek(self):
        """查看队首元素（不删除）"""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.head.value

    def is_empty(self):
        """判断队列是否为空"""
        return self._size == 0

    def __len__(self):
        """返回队列长度"""
        return self._size

    def __str__(self):
        """可视化队列内容（调试用）"""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) if values else "Empty Queue"