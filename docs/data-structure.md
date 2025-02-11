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

- **后进先出（LIFO）**的线性结构。
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

- **先进先出（FIFO）**的线性结构。
- **核心操作**：`enqueue`（入队）、`dequeue`（出队）。

### **代码示例**

```python
from collections import deque
queue = deque()
queue.append(1)    # 入队
queue.append(2)
front = queue[0]   # 查看队首
queue.popleft()    # 出队 -> 1
```

### **变种队列**

- **双端队列 (Deque)**：两端均可插入/删除。
- **优先队列 (Priority Queue)**：按优先级出队（通常用堆实现）。

### **应用场景**

- 任务调度、消息队列
- BFS（广度优先搜索）

------

## **5. 哈希表 (Hash Table)**

### **定义**

- 通过**键（Key）直接访问值（Value）**的数据结构。
- **核心思想**：哈希函数将键映射到存储位置。

### **冲突解决**

- **开放寻址法**：冲突时寻找下一个空槽。
- **链地址法**：每个槽存储链表（如Python的字典）。

### **代码示例**

```python
# Python字典即哈希表实现
hash_map = {}
hash_map["apple"] = 1  # 插入
hash_map["banana"] = 2
print(hash_map.get("apple"))  # 获取 -> 1
del hash_map["banana"]        # 删除
```

### **应用场景**

- 快速查找（如数据库索引）
- 统计频率（如字母异位词分组）

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

- 由**顶点（Vertex）**和**边（Edge）**组成的非线性结构。
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