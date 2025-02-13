---
title: 数据结构
order: 2
---

## **1. 数组 (Array)**

### **定义**

- 一组**连续内存空间**存储的**相同类型元素**的集合。
- **特点**：通过下标（索引）快速访问元素，但大小固定（静态数组）或可扩展（动态数组）。

### **核心操作**

| 操作     | 时间复杂度 | 说明                           |
| :------- | :--------- | :----------------------------- |
| 访问元素 | O(1)       | 通过索引直接访问（如`arr[3]`） |
| 插入元素 | O(n)       | 需要移动后续元素               |
| 删除元素 | O(n)       | 同上                           |
| 查找元素 | O(n)       | 遍历查找（无序数组）           |

### **代码示例**

```python
# 创建数组
arr = [1, 2, 3, 4]

# 访问元素
print(arr[0])  # 输出 1

# 插入元素（在末尾添加）
arr.append(5)   # O(1)（动态数组均摊时间）
arr.insert(2, 10)  # O(n)（插入到中间）

# 删除元素
arr.pop()      # 删除末尾元素 O(1)
arr.pop(0)     # 删除第一个元素 O(n)
```

### **应用场景**

- 需要快速随机访问（如矩阵运算）
- 数据量已知或变化较小的场景

------

## **2. 链表 (Linked List)**

### **定义**

- 由**节点**组成的数据结构，每个节点包含**数据**和**指向下一个节点的指针**。
- **特点**：内存非连续，插入/删除高效，但访问元素需要遍历。

### **类型**

- **单链表**：每个节点指向下一个节点。
- **双链表**：节点同时指向前驱和后继。
- **循环链表**：尾节点指向头节点。

### **核心操作**

| 操作      | 时间复杂度 | 说明                       |
| :-------- | :--------- | :------------------------- |
| 访问元素  | O(n)       | 从头节点开始遍历           |
| 插入/删除 | O(1)       | 已知前驱节点时（如双链表） |
| 查找元素  | O(n)       | 必须遍历                   |

### **代码示例（单链表）**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 创建链表：1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# 插入节点（在节点2后插入4）
node = head.next
new_node = ListNode(4)
new_node.next = node.next
node.next = new_node  # 链表变为1 -> 2 -> 4 -> 3

# 删除节点（删除节点4）
node.next = node.next.next  # 链表恢复为1 -> 2 -> 3
```

### **应用场景**

- 频繁插入/删除的场景（如LRU缓存）
- 实现栈、队列等数据结构

------

## **3. 栈 (Stack)**

### **定义**

- **后进先出(LIFO)**的线性结构。
- **核心操作**：`push`（入栈）、`pop`（出栈）、`peek`（查看栈顶）。

### **代码示例**

```python
# 用列表模拟栈
stack = []
stack.append(1)   # push 1
stack.append(2)   # push 2
top = stack[-1]   # peek -> 2
stack.pop()       # pop -> 2
```

### **应用场景**

- 函数调用栈
- 括号匹配、表达式求值（如逆波兰表达式）

------

## **4. 队列 (Queue)**

### **定义**

- **先进先出(FIFO)**的线性结构。
- **核心操作**：`enqueue`（入队）、`dequeue`（出队）。

### **代码示例**

使用 deque ：

```python
from collections import deque
queue = deque()
queue.append(1)    # 入队
queue.append(2)
front = queue[0]   # 查看队首
queue.popleft()    # 出队 -> 1
```

简单形式（通过列表实现）：

```python
# 简单的通过列表实现
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
q.dequeue()
q.view()
```

由于上面入队列的时间复杂度是O(n) ，可以再简单优化一下，通过 `popleft` 和 `append`：（这里改为了deque）

```python
# 通过将列表中的insert替换成 popleft 和 append 降低时间复杂度。
from collections import deque

class Queue:
    
    def __init__(self):
        self.queue = deque()
    
    def consumer(self):
        if len(self.queue) == 0:
            return None
        return self.queue.popleft()  # 从队头移除元素
    
    def producer(self, value):
        self.queue.append(value)  # 向队尾添加元素
```

还可以基于 链表 实现：

```python
# 还可以基于链表实现
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
```

### **变种队列**

- **双端队列 (Deque)**：两端均可插入/删除。
- **优先队列 (Priority Queue)**：按优先级出队（通常用堆实现）。

### **应用场景**

- 任务调度、消息队列
- BFS（广度优先搜索）

------

## **5. 哈希表 (Hash Table)**

### 5.1 哈希表 概念

**定义**

- 通过**键(Key)直接访问值(Value)**的数据结构。
- **核心思想**：哈希函数将键映射到存储位置。

**冲突解决**

- **开放寻址法**：冲突时寻找下一个空槽。
- **链地址法**：每个槽存储链表（如Python的字典）。

**代码示例**

```python
# Python字典 即哈希表实现
hash_map = {}
hash_map["apple"] = 1  # 插入
hash_map["banana"] = 2
print(hash_map.get("apple"))  # 获取 -> 1
del hash_map["banana"]        # 删除
```

**应用场景**

- 快速查找（如数据库索引）
- 统计频率（如字母异位词分组）

### **5.2 链地址法（Chaining）**

#### **核心思想**

- 每个数组的索引位置（称为“桶”）不再直接存储单个键值对，而是存储一个**链表**（或红黑树等其他数据结构）。
- 当多个键的哈希值冲突时，它们会被添加到同一个桶的链表中。

#### **具体操作**

1. **插入键值对**：
   - 计算键的哈希值，找到对应桶。
   - 如果桶为空，直接存入链表头节点。
   - 如果桶不为空，遍历链表：
     - 如果发现键已存在，更新值。
     - 如果不存在，将新键值对添加到链表末尾（或头部）。
2. **查找键值对**：
   - 计算键的哈希值，找到对应桶。
   - 遍历链表，逐个比较键是否匹配。

#### **代码示例（Python简化版）**

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # 每个桶是一个列表（模拟链表）

    def _hash(self, key):
        return hash(key) % self.size  # 哈希函数

    def put(self, key, value):
        bucket_idx = self._hash(key)
        bucket = self.table[bucket_idx]
        # 遍历链表，检查是否已存在该键
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # 更新键值对
                return
        bucket.append((key, value))  # 添加新键值对

    def get(self, key):
        bucket_idx = self._hash(key)
        bucket = self.table[bucket_idx]
        for k, v in bucket:
            if k == key:
                return v
        return None  # 未找到
```

**为什么链地址法不会导致效率低下？**

虽然链表需要遍历，但哈希表的设计目标是通过以下两点保证高效性：

**(1) 哈希函数的均匀性**

- 好的哈希函数会将键**均匀分布**到各个桶中，避免大量冲突。
- 例如，Python的哈希函数对字符串、整数等类型有优化，冲突概率极低。

**(2) 负载因子（Load Factor）控制**

- **负载因子** = 哈希表中元素数量 / 桶的数量。
- 当负载因子超过阈值（如0.75），哈希表会触发**扩容（Rehashing）**：
  - 创建一个更大的桶数组（例如翻倍）。
  - 将所有键值对重新哈希到新桶中。
- 扩容后，冲突概率显著降低，链表长度保持较短（通常为0-2个节点）。

现代哈希表（如Java的`HashMap`）会进一步优化链地址法：

- **链表转红黑树（Java）**：当链表长度超过阈值（如8），将链表转换为红黑树，将查找时间从`O(n)`优化为`O(log n)`。
- **动态扩容策略**：根据负载因子智能调整桶的数量，平衡时间和空间。

### 5.3 开放地址法（Open Addressing）

#### **核心思想**

开放地址法的思想是，当发生冲突时，**寻找另一个空的数组位置**来存储冲突的元素。常见的解决方法有**线性探测法**、**二次探测法**和**双重哈希法**等。

#### **具体实现**

- **插入**：当插入新元素时，计算哈希值，如果该位置已经被占用，就按照预定的探测策略（如线性探测）尝试查找下一个空的位置。
- **查找**：查找时，先计算哈希值，如果当前位置的元素就是我们要查找的键，就直接返回值。如果当前位置不匹配，就根据探测策略继续查找其他位置，直到找到目标或确认该键不存在。

#### **代码示例（Python简化版）**

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size  # 每个桶直接存储键值对或标记

    def _hash(self, key):
        return hash(key) % self.size

    def _probe(self, start_idx):
        """线性探测下一个可用位置"""
        idx = start_idx
        while True:
            if self.table[idx] is None or self.table[idx] == "DELETED":
                return idx
            idx = (idx + 1) % self.size  # 回绕到数组开头
            if idx == start_idx:  # 整个表已满
                raise Exception("Hash table is full")

    def put(self, key, value):
        start_idx = self._hash(key)
        idx = start_idx

        # 查找可插入的位置或更新现有键
        while True:
            if self.table[idx] is None or self.table[idx] == "DELETED":
                # 插入新键值对
                self.table[idx] = (key, value)
                return
            elif self.table[idx][0] == key:
                # 键已存在，更新值
                self.table[idx] = (key, value)
                return
            idx = (idx + 1) % self.size # 通过取余方式能够遍历整个数组
            if idx == start_idx:
                raise Exception("Hash table is full")

    def get(self, key):
        start_idx = self._hash(key)
        idx = start_idx

        while True:
            entry = self.table[idx]
            if entry is None:
                return None  # 未找到
            elif entry != "DELETED" and entry[0] == key:
                return entry[1]  # 返回找到的值
            idx = (idx + 1) % self.size
            if idx == start_idx:
                return None  # 遍历完整个表未找到
```

------

## **6. 二叉树 (Binary Tree)**

### **定义**

- 每个节点最多有**两个子节点**（左子节点、右子节点）。
- **特殊类型**：
  - **二叉搜索树 (BST)**：左子树所有节点 < 根节点 < 右子树所有节点。
  - **平衡二叉树**（如AVL树、红黑树）：通过旋转保持高度平衡。

### **遍历方式**

| 遍历方式 | 顺序                     |
| :------- | :----------------------- |
| 前序遍历 | 根 -> 左 -> 右           |
| 中序遍历 | 左 -> 根 -> 右           |
| 后序遍历 | 左 -> 右 -> 根           |
| 层序遍历 | 按层级从上到下、从左到右 |

### **代码示例（二叉树节点）**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 创建二叉树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
```

### **应用场景**

- 文件系统结构
- 表达式树（用于计算）

------

## **7. 堆 (Heap)**

### **定义**

- 一种**完全二叉树**，满足：
  - **最大堆**：父节点值 ≥ 子节点值。
  - **最小堆**：父节点值 ≤ 子节点值。

:::tip

完全二叉树是指除了最后一层外，其他层的节点都是 **满的**，并且最后一层的节点 **尽可能靠左排列**。

:::

### **核心操作**

| 操作     | 时间复杂度 | 说明                  |
| :------- | :--------- | :-------------------- |
| 插入元素 | O(log n)   | 上浮调整（sift up）   |
| 删除堆顶 | O(log n)   | 下沉调整（sift down） |

### **代码示例（Python的 `heapq` 模块）**

```python
import heapq

# 最小堆
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))  # 输出1
```

### **应用场景**

- 优先队列
- Top K问题（如最大的K个元素）

------

## **8. 图 (Graph)**

### **定义**

- 由 **顶点(Vertex)** 和 **边(Edge)** 组成的非线性结构。
- **表示方式**：
  - **邻接矩阵**：二维数组表示顶点连接关系。
  - **邻接表**：为每个顶点维护一个链表，记录其邻居。

### **常见算法**

- **遍历**：DFS（深度优先）、BFS（广度优先）
- **最短路径**：Dijkstra（无负权边）、Bellman-Ford（含负权边）
- **最小生成树**：Prim算法、Kruskal算法

### **代码示例（邻接表表示图）**

```python
# 使用字典表示邻接表
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

# DFS遍历
def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

dfs(graph, 'A', set())  # 输出A -> B -> D -> C -> E
```

### **应用场景**

- 社交网络（顶点为用户，边为好友关系）
- 路径规划（如地图导航）