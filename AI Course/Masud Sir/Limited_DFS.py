tree = {
    'A' : ['B', 'E'],
    'B' : ['C', 'D'],
    'C' : ['F'],
    'D' : [],
    'F' : [],
    'E' : []
}

def lim_dfs(tree,start,limit):
    visited = set()
    stack = [(start, 0)]

    while stack:
        node, depth = stack.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            if depth < limit:
                for child in tree[node]:
                    stack.append((child, limit + 1))

    print(f"Limited DFS is complete for limit = {limit}")


lim_dfs(tree,"A",2)