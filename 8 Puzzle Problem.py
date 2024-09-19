import heapq

# Function to calculate the Manhattan distance (heuristic function)
def manhattan_distance(start, goal):
    distance = 0
    for i in range(1, 9):  # Numbered tiles from 1 to 8
        sx, sy = divmod(start.index(i), 3)
        gx, gy = divmod(goal.index(i), 3)
        distance += abs(sx - gx) + abs(sy - gy)
    return distance

# Function to get possible moves for a given board state
def get_neighbors(state):
    neighbors = []
    index = state.index(0)  # Find the empty space (0)
    x, y = divmod(index, 3)  # Get row and column of the empty space

    moves = {
        'up': (x - 1, y),
        'down': (x + 1, y),
        'left': (x, y - 1),
        'right': (x, y + 1),
    }

    for move, (new_x, new_y) in moves.items():
        if 0 <= new_x < 3 and 0 <= new_y < 3:  # Ensure move is within the grid
            new_index = new_x * 3 + new_y
            new_state = list(state)
            # Swap empty space (0) with the target tile
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))

    return neighbors

# A* algorithm to solve the 8-puzzle problem
def a_star(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        if current == goal:
            break

        for neighbor in get_neighbors(current):
            new_cost = cost_so_far[current] + 1

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + manhattan_distance(neighbor, goal)
                heapq.heappush(priority_queue, (priority, neighbor))
                came_from[neighbor] = current

    return reconstruct_path(came_from, start, goal)

# Function to reconstruct the path to the goal
def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Function to print the board state
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

if __name__ == "__main__":
    # Initial state and goal state
    start = (1, 2, 3,
             4, 0, 5,
             6, 7, 8)  # The 0 represents the empty space

    goal = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)  # Solved puzzle

    print("Initial board:")
    print_board(start)

    path = a_star(start, goal)

    print("Steps to solve the puzzle:")
    for state in path:
        print_board(state)
