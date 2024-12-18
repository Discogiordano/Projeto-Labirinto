import random

def generate_maze(width, height):
    """
    Gera um labirinto usando busca em profundidade recursiva.
    """
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def carve_passages(cx, cy):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx * 2, cy + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[cy + dy][cx + dx] = 0
                maze[ny][nx] = 0
                carve_passages(nx, ny)

    maze[1][1] = 0
    carve_passages(1, 1)
    return maze
