class HashTable:
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
    

class HashTable: 
    
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size # 哈希函数
    
    # 线性探测法
    def _open_addressing(self, key, value, index_idx, index):
        # 匹配键是否正确
        if "key" in index:
            if index['key'] == key:
                # 直接更新
                index['value'] = value
            else:
                # 递归 + 1 
                self._open_addressing(key, value, index_idx + 1, index)
        else: 
            index['key'] = key
            index['value'] = value
    
    # put方法
    def put(self, key, value):
        index_idx = self._hash(key)
        index = self.table[index_idx]
        self._open_addressing(key, value, index_idx, index)



        
        
        
            
