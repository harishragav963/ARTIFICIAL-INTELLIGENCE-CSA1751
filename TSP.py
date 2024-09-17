import itertools

# Function to calculate the total distance of a given path
def calculate_total_distance(graph, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    total_distance += graph[path[-1]][path[0]]  # Return to the starting city
    return total_distance

# Function to solve TSP using brute-force
def traveling_salesman(graph):
    # Get all cities (nodes)
    cities = list(graph.keys())
    
    # Generate all possible permutations of the cities
    all_possible_paths = itertools.permutations(cities)
    
    # Initialize variables to store the shortest path and its distance
    shortest_path = None
    shortest_distance = float('inf')
    
    # Iterate through all permutations of cities
    for path in all_possible_paths:
        current_distance = calculate_total_distance(graph, path)
        
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_path = path
    
    # Return the shortest path and its distance
    return shortest_path, shortest_distance

# Example usage:
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

# Solve the TSP problem
shortest_path, shortest_distance = traveling_salesman(graph)

# Print the result
print(f"Shortest Path: {' -> '.join(shortest_path)} -> {shortest_path[0]}")
print(f"Total Distance: {shortest_distance}")