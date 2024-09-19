import random

class VacuumCleaner:
    def __init__(self, grid_size=5):
        self.grid_size = grid_size
        # Initialize a grid with 0 (clean) and 1 (dirty)
        self.grid = [[random.choice([0, 1]) for _ in range(grid_size)] for _ in range(grid_size)]
        # Start vacuum cleaner at a random position
        self.vacuum_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
        self.cleaned_rooms = 0

    def display_grid(self):
        for row in self.grid:
            print(row)
        print()

    def is_dirty(self, x, y):
        return self.grid[x][y] == 1

    def clean(self, x, y):
        if self.is_dirty(x, y):
            self.grid[x][y] = 0
            self.cleaned_rooms += 1
            print(f"Cleaned room at ({x}, {y})")
        else:
            print(f"Room at ({x}, {y}) is already clean")

    def move(self):
        x, y = self.vacuum_position
        if x < self.grid_size - 1:
            x += 1
        elif y < self.grid_size - 1:
            x = 0
            y += 1
        else:
            x, y = 0, 0  # Restart from the top-left corner if all rows are done
        self.vacuum_position = [x, y]
        print(f"Vacuum moved to ({x}, {y})")

    def clean_grid(self):
        total_dirty_rooms = sum(row.count(1) for row in self.grid)
        print("Initial grid:")
        self.display_grid()

        while self.cleaned_rooms < total_dirty_rooms:
            x, y = self.vacuum_position
            self.clean(x, y)
            self.move()

        print("All rooms cleaned!")
        self.display_grid()

if __name__ == "__main__":
    vacuum = VacuumCleaner()
    vacuum.clean_grid()
