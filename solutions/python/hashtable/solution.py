"""基于链地址法："""
class HashTable_Link:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # 每个桶是一个列表（模拟链表）

    def _hash(self, key):
        return hash(key) % self.size  # 哈希函数

    def put(self, key, value):
        # 基于链表地址法的HashTable，数组索引对应的位置叫做 桶 。 
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
    
"""基于开放寻址法的线性探测法的方式："""
class HashTable_Detect:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size  

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
        
        
            
