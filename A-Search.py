import heapq

def a_star(graph, start, goal, heuristic):
    # Priority queue to store nodes to be explored
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    # Dictionary to store the cost of the shortest path to each node
    g_costs = {start: 0}
    
    # Dictionary to store the parent of each node for path reconstruction
    parents = {start: None}
    
    while open_list:
        # Get the node with the lowest f value (g + h)
        current_cost, current_node = heapq.heappop(open_list)
        
        # If the goal is reached, reconstruct the path
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parents[current_node]
            return path[::-1]
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            tentative_g_cost = g_costs[current_node] + weight
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_cost, neighbor))
                parents[neighbor] = current_node
    
    return None  # Return None if no path is found

# Example heuristic function (simple heuristic for demonstration)
def heuristic(node, goal):
    # This is a placeholder heuristic function
    # For a real-world scenario, you need a meaningful heuristic
    return 0

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 2)],
    'D': [('F', 1)],
    'E': [('F', 2)],
    'F': []
}

# Define start and goal nodes
start = 'A'
goal = 'F'

# Run A* search
path = a_star(graph, start, goal, heuristic)
print("Path found:", path)
