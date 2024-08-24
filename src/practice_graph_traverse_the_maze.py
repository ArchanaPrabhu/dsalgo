from collections import deque

def bfs_shortest_path(maze, start, end):
    # Define the directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(maze), len(maze[0])

    # Initialize the queue with the start position and the initial distance of 0
    queue = deque([(start[0], start[1], 0)])

    # Set to track visited positions
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        r, c, dist = queue.popleft()

        # If we reach the end position, return the distance
        if (r, c) == end:
            return dist

        # Explore all four directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            print(r, c, " to ", nr, nc)

            # Check if the new position is within bounds and not visited or a wall
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and maze[nr][nc] == 0:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    # If the end is not reachable, return -1
    return -1

def solve():
    # Example maze (0 = open path, 1 = wall)
    # You can move only up, down, right, left, no diagonals
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    end = (4, 4)

    shortest_path_length = bfs_shortest_path(maze, start, end)
    print("Shortest path length:", shortest_path_length)

if __name__ == "__main__":
    solve()
