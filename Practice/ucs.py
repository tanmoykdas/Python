import heapq

def ucs(graph, start, goal):
    queue = [(0, start)]  # (cost, node)
    visited = set()
    costs = {start: 0}
    parent = {start: None}

    while queue:
        cost, node = heapq.heappop(queue)
        if node == goal:
            # Reconstruct path
            path = []
            while node:
                path.append(node)
                node = parent[node]
            path.reverse()
            print(f"Path: {path}, Total cost: {cost}")
            return path, cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(queue, (new_cost, neighbor))
    print("No path found.")
    return None, float('inf')

# Example graph: each edge is (neighbor, cost)
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 2)],
    'D': [('G', 2)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}

ucs(graph, 'A', 'G')
