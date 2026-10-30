def path_exists(graph, start, target):
    
    if start == target:
        return False
    queue = [start]
    visited = set([start])
    while queue:
        current_node = queue.pop(0)
        for neighbor in graph.get(current_node, []):
            if neighbor == target:
                return True  
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return False

my_graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": ["F"], "E": [], "F": []}

print(path_exists(my_graph, start="D", target="A"))
