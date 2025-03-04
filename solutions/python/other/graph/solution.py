import heapq

def dijkstra(graph, start):
    # 初始化
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # 优先队列，存储 (距离, 节点)
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)  # 获取当前最小距离节点
        
        # 如果当前距离已经大于已知最短距离，跳过
        if current_distance > distances[current_node]:
            continue
        
        # 遍历当前节点的邻居
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # 如果通过当前节点到邻居的路径更短，更新距离
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# 图的表示（邻接表）
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 计算从 'A' 出发的最短路径
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print("从节点", start_node, "到其他节点的最短路径:")
for node, distance in shortest_paths.items():
    print(f"到 {node}: {distance}")
