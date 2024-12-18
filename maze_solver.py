from collections import deque  # Importa deque para a fila

def solve_maze(maze):
    """
    Resolve o labirinto usando busca em largura (BFS).
    """
    height, width = len(maze), len(maze[0])
    start, end = (1, 1), (height - 2, width - 2)  # Define início e fim
    queue = deque([start])  # Inicializa a fila com a posição inicial
    visited = set()  # Mantém as células visitadas
    came_from = {}  # Rastreia o caminho percorrido

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Movimentos possíveis

    while queue:
        cx, cy = queue.popleft()  # Remove a próxima célula da fila
        if (cx, cy) == end:  # Se chegou ao fim, para a busca
            break
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy  # Calcula a próxima posição
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny))  # Adiciona a posição na fila
                visited.add((nx, ny))  # Marca como visitada
                came_from[(nx, ny)] = (cx, cy)  # Salva a posição anterior

    # Reconstrói o caminho do final ao início
    path = []
    current = end
    while current != start:
        path.append(current)
        current = came_from.get(current, start)
    path.append(start)
    path.reverse()  # Inverte para obter o caminho na ordem certa
    return path  # Retorna o caminho
