tree = {
    'A' : ['B', 'E'],
    'B' : ['C', 'D'],
    'C' : ['F'],
    'D' : [],
    'F' : [],
    'E' : []
}


def idfs(tree, start, limit):
    for i in range(limit):
        print(f"depth limit {i + 1}")
        visited = set()
        stack = [(start, 0)]
        while stack:
            node, depth = stack.pop(0)
            if node not in visited:
                print(node)
                visited.add(node)
                if depth < i:
                    for child in tree[node]:
                        stack.append((child, depth + 1))


idfs(tree,"A", 3)