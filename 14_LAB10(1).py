"""
Задача №1
Написати програму для пошуку найкоротшого шляху
між двома заданими вершинами
Автор: Мотовилець Марія 31І групa
"""
import heapq

# Граф 
graph = {
    'A': {'B': 2, 'C': 1, 'D': 2},
    'B': {'A': 2, 'D': 3},
    'C': {'A': 1, 'G': 1},
    'D': {'B': 3, 'A': 2, 'F': 1},
    'F': {'D': 1, 'G': 3, 'H': 2},
    'G': {'F': 2, 'C': 1, 'H': 2},
    'H': {'G': 2, 'F': 2},
}

start = 'C'
end = 'B'

queue = [(0, start)]
dist = {v: float('infinity') for v in graph}
dist[start] = 0
path = {}

while queue:
    dist_cur, vertex_cur = heapq.heappop(queue)

    if dist_cur > dist[vertex_cur]:
        continue

    for neighbor, weight in graph[vertex_cur].items():
        distance = dist_cur + weight

        if distance < dist[neighbor]:
            dist[neighbor] = distance
            heapq.heappush(queue, (distance, neighbor))
            path[neighbor] = vertex_cur

shortest_path, vertex_curr = [], end
while vertex_curr in path:
    shortest_path.insert(0, vertex_curr)
    vertex_curr = path[vertex_curr]
if shortest_path:
    shortest_path.insert(0, start)

print(f"Найкоротший шлях між {start} і {end}: {shortest_path} з відстанню {dist[end]}")
