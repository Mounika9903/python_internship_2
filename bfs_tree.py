class Graph:
    def __init__(self, graph):
        self.graph = graph
    
    def bfs(self, start):
        visited = set()
        stack = [start]  
        
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)


graph_data = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

graph = Graph(graph_data)
start_node = 'A'
print("BFS Traversal:")
graph.bfs(start_node)
