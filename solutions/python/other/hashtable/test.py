from solution import HashTable_Link, HashTable_Detect

a,b,c = ("张三", "李四", "王五")

# 链地址测试：
link = HashTable_Link(10)
link.put(a, 1)
link.put(b, 2)
link.put(c, 3)
print(f'{a}: {link.get(a)}')
print(f'{b}: {link.get(b)}')
print(f'{c}: {link.get(c)}')
link.put(a, 10)
print(f'{a}: {link.get(a)}')

# 寻址测试：
detect = HashTable_Detect(10)
detect.put(a, 1)
detect.put(b, 2)
detect.put(c, 3)
print(f'{a}: {detect.get(a)}')
print(f'{b}: {detect.get(b)}')
print(f'{c}: {detect.get(c)}')
detect.put(a, 10)
print(f'{a}: {detect.get(a)}')
