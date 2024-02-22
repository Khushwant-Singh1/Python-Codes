import sys
from PIL import Image, ImageDraw

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier(): #
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Maze():
    def __init__(self, filename):
        # Read file and set height and width of maze
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") !=1:
            raise Exception("maze must have exactly one goal")

        # Determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("|", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i,j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row,col = state

        # All possible actions
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        # Ensure actions are valid
        result = []
        for action, (r, c) in candidates:
            try:
                if not self.walls[r][c]:
                    result.append((action,(r,c)))
            except IndexError:
                continue
        return result

    def solve(self):
        """Finds a solution to maze, if one exists"""

        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        self.explored = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []

                # Follow parent nodes to find solution
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions,cells)
                return

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    def output_image(self, filename, show_solution=True, show_explored=False):
        # Create an image with the appropriate dimensions
        cell_size = 50
        img = Image.new("RGB", (self.width * cell_size, self.height * cell_size), "white")
        draw = ImageDraw.Draw(img)

        # Draw walls, start, and goal
        for i in range(self.height):
            for j in range(self.width):
                if self.walls[i][j]:
                    draw.rectangle([(j * cell_size, i * cell_size), ((j + 1) * cell_size, (i + 1) * cell_size)], fill="black")
                if (i, j) == self.start:
                    draw.ellipse([(j * cell_size + cell_size // 4, i * cell_size + cell_size // 4), ((j + 1) * cell_size - cell_size // 4, (i + 1) * cell_size - cell_size // 4)], fill="green")
                if (i, j) == self.goal:
                    draw.ellipse([(j * cell_size + cell_size // 4, i * cell_size + cell_size // 4), ((j + 1) * cell_size - cell_size // 4, (i + 1) * cell_size - cell_size // 4)], fill="red")

        # Draw solution path
        if show_solution and self.solution:
            actions, cells = self.solution
            for action, (i, j) in zip(actions, cells):
                x_center = j * cell_size + cell_size // 2
                y_center = i * cell_size + cell_size // 2
                if action == "up":
                    y_center -= cell_size // 2
                elif action == "down":
                    y_center += cell_size // 2
                elif action == "left":
                    x_center -= cell_size // 2
                elif action == "right":
                    x_center += cell_size // 2
                draw.line([(cells[0][1] * cell_size + cell_size // 2, cells[0][0] * cell_size + cell_size // 2), (x_center, y_center)], fill="blue", width=3)
                draw.ellipse([(j * cell_size + cell_size // 4, i * cell_size + cell_size // 4), ((j + 1) * cell_size - cell_size // 4, (i + 1) * cell_size - cell_size // 4)], fill="blue")

        # Draw explored cells
        if show_explored:
            for i in range(self.height):
                for j in range(self.width):
                    if (i, j) in self.explored and (i, j) != self.start and (i, j) != self.goal:
                        draw.ellipse([(j * cell_size + cell_size // 4, i * cell_size + cell_size // 4), ((j + 1) * cell_size - cell_size // 4, (i + 1) * cell_size - cell_size // 4)], fill="yellow")

        # Save image to file
        img.save(filename)

# Example usage:
maze = Maze("maze1.txt")
maze.solve()
maze.output_image("maze_solution.png", show_solution=True, show_explored=True)
