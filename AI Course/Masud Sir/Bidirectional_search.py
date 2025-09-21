un_tree = {
    'A' : ['B', 'E'],
    'B' : ['C', 'D','A'],
    'C' : ['F','B'],
    'D' : ['B'],
    'E' : ['A'],
    'F' : ['C']
}

def bidirectional(tree,start,goal):
    start_visited = set()
    goal_visited = set()

    start_queue = [start]
    goal_queue = [goal]

    while start_queue and goal_queue:
        start_node = start_queue.pop(0)
        if start_node not in start_visited:
            start_visited.add(start_node)
            for child in tree[start_node]:
                if child not in start_visited:
                    start_queue.append(child)
        
        goal_node = goal_queue.pop(0)
        if goal_node not in goal_visited:
            goal_visited.add(goal_node)
            for child in tree[goal_node]:
                if child not in goal_visited:
                    goal_queue.append(child)

        if start_node in goal_visited or goal_node in start_visited:
            return start_visited,goal_visited

print(bidirectional(un_tree, "A", "F"))