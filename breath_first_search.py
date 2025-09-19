from collections import deque

def bfs(graph, start):
    visited = set()        # To keep track of visited nodes
    queue = deque([start]) # Initialize queue with start node

    while queue:
        vertex = queue.popleft()  # Remove from queue
        if vertex not in visited:
            print(vertex, end=" ")   # Process the node
            visited.add(vertex)

            # Add all unvisited neighbors to queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS Traversal starting from A:")
bfs(graph, 'A')
