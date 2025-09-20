tree = {
    'A' : ['B', 'E'],
    'B' : ['C', 'D'],
    'C' : ['F'],
    'D' : [],
    'F' : [],
    'E' : []
}

def dfs(tree,strat):
    visited = set()
    stack = [strat]

    while stack:
        node = stack.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            stack.extend(tree[node])
    print("DFS complete")


dfs(tree,"A")