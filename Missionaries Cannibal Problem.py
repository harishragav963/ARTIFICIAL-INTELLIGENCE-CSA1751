from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, depth=0):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.depth = depth

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries > 0 and self.missionaries < self.cannibals:
            return False
        if (3 - self.missionaries) > 0 and (3 - self.missionaries) < (3 - self.cannibals):
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def bfs(initial_state):
    queue = deque([initial_state])
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            return current_state.depth

        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    if current_state.boat == 1:
                        new_state = State(current_state.missionaries - m, current_state.cannibals - c, 0, current_state.depth + 1)
                    else:
                        new_state = State(current_state.missionaries + m, current_state.cannibals + c, 1, current_state.depth + 1)

                    if new_state.is_valid() and new_state not in visited:
                        queue.append(new_state)
                        visited.add(new_state)

    return -1

def get_input():
    missionaries = int(input("Enter the number of missionaries: "))
    cannibals = int(input("Enter the number of cannibals: "))
    boat = int(input("Enter the boat position (1 for starting side, 0 for other side): "))
    return State(missionaries, cannibals, boat)

if __name__ == "__main__":
    initial_state = get_input()
    result = bfs(initial_state)
    if result != -1:
        print(f"Solution found in {result} steps.")
    else:
        print("No solution found.")
