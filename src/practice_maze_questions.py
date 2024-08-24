from collections import deque

def solution():
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    directions = [(0, 1), (1, 0), (1, 1), (-1, 0)]

    # visited, queue (0, 0)
    visited = set()
    q = deque()
    q.append((0,0)) # [(0,0), (1,0)]

    rows = len(maze)
    col = len(maze[0])
    while len(q) > 0:
        cr, cc = q.popleft()
        visited.add((cr, cc))
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if (nr, nc) not in visited and nr < rows and nc < col and maze[nr][nc] == 0:
                q.append(nr, nc)

def dfs(pair, maze, visited):
    directions = [(1, 0), (0, 1), (1, 1)]
    stack = [tuple(pair)]
    # print("stack", pair, len(stack))
    count = 1
    while stack:
        print(stack)
        cr, cc = stack.pop()
        visited.add((cr, cc))
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and (nr, nc) not in visited and maze[nr][nc] == 1:
                stack.append((nr, nc))
                count = count + 1
    print("pair", pair, "count", count)
    return count

def islands_of_ones(maze):
    visited = set()
    ans = []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (i, j) not in visited and maze[i][j] == 1:
                visited.add((i, j))
                ans.append(dfs((i, j), maze, visited))
                print("visited", visited)
    print(ans)

if __name__ == "__main__":
    # solution()
    maze = [
        [1, 0, 0],
        [0, 0, 1],
        [1, 1, 0]
    ]
    islands_of_ones(maze)