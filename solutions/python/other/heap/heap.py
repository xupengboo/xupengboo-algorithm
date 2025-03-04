class heapq:

    def __init__(self):
        self.heap = []

    # 堆插入： 将新元素插入到树的最底层最左边（数组末尾）
    def insert(self, value):
        self.heap.append(value)
        self._shif_up(len(self.heap) - 1)

    # 堆上浮操作
    def _shif_up(self, idx):
        while idx > 0:
            """
                父节点的下标：`parent(i) = (i - 1) // 2`
            """
            parent = (idx - 1) // 2 # 计算父节点索引
            if self.heap[idx] > self.heap[parent]: # 最大堆：子节点大于父节点
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx] # 交换值
                idx = parent
            else:
                # 已满足堆的性质
                break

    # 删除堆：移除根节点，并且将最后一个节点放到第一个节点上
    def pop(self):
        if not self.heap:
            return None
        max_val = self.heap[0] # 保留栈顶元素（最大值）
        self.heap[0] = self.heap[-1] # 将末尾元素移到堆顶
        self.heap.pop()
        self._shif_down(0)
        return max_val
        
    # 堆下沉操作
    def _shif_down(self, idx):
        n = len(self.heap)
        while True:
            """
                左子节点的下标：`left(i) = 2 * i + 1`
                右子节点的下标：`right(i) = 2 * i + 2`
            """
            left = 2 * idx + 1      # 左子节点索引
            right = 2 * idx + 2     # 右子节点索引
            largest = idx           # 当前节点、左子、右子中的最大值索引
            
            # 比较左子节点
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            
            # 比较右子节点
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            
            # 如果最大值不是当前节点，交换并继续下沉
            if largest != idx:
                self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
                idx = largest
            else:
                # 当前节点已满足堆性质
                break

    def build_heap(self, arr):
        """通过Floyd算法将无序数据构建为堆（时间复杂度O(n)）"""
        self.heap = arr.copy()
        # Floyd算法：从最后一个非叶子节点开始下沉调整
        for i in range((len(self.heap) - 1) // 2, -1, -1):  # range(起始值, 结束值, 步长)
            self._shif_down(i)

    def __str__(self):
        return str(self.heap)

# 测试插入和删除
heap = heapq()
heap.insert(3)
heap.insert(1)
heap.insert(5)
heap.insert(2)
print(heap)          # 输出: [5, 2, 3, 1]
print(heap.pop())  # 输出: 5
print(heap)          # 输出: [3, 2, 1]

# 测试构建堆
arr = [4, 1, 7, 3, 9, 2]
heap.build_heap(arr)
print(heap)          # 输出: [9, 4, 7, 3, 1, 2]

