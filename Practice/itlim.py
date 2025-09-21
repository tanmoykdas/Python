tree = {
    'A' : ['B', 'E'],
    'B' : ['C', 'D'],
    'C' : ['F'],
    'D' : [],
    'F' : [],
    'E' : []
}

def iterative_limited_dfs(tree, start, max_limit):
    for limit in range(max_limit + 1):
        print(f"\nDepth limit: {limit}")
        visited = set()
        stack = [(start, 0)]
        while stack:
            node, depth = stack.pop(0)
            if node not in visited:
                print(node)
                visited.add(node)
                if depth < limit - 1:
                    for child in tree[node]:
                        stack.append((child, depth + 1))
        print(f"Iterative Limited DFS complete for limit={limit}")

iterative_limited_dfs(tree, "A", 2)
