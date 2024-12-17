from collections import deque

def solve_maze(maze):
    height, width = len(maze), len(maze[0])
    start, end = (1, 1), (height - 2, width - 2)
    queue = deque([start])
    visited = set()
    came_from = {}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        cx, cy = queue.popleft()
        if (cx, cy) == end:
            break
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                came_from[(nx, ny)] = (cx, cy)

    path = []
    current = end
    while current != start:
        path.append(current)
        current = came_from.get(current, start)
    path.append(start)
    path.reverse()
    return path
