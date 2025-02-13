from solution import Queue

# 测试
q = Queue()

# 1. 入队操作
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
# 查看队首元素
print(q.peek())

# 2. 出队操作
q.dequeue()
# 查看队首元素
print(q.peek())