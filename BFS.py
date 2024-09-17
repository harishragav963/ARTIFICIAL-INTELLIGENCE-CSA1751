from collections import deque

def bfs(graph, start_node):
    # Create a queue for BFS
    queue = deque([start_node])
    
    # Set to keep track of visited nodes
    visited = set([start_node])
    
    # While the queue is not empty
    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        print(node, end=" ")  # Process the node (e.g., print it)
        
        # Get all adjacent nodes of the dequeued node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # If the neighbor hasn't been visited, mark it visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call the BFS function
start_node = 'A'
print("THE SHORTEST PATH IS: ")
bfs(graph, start_node)
