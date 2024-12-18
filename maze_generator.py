import random  # Importa o módulo random para embaralhar direções

def carve_passages_iterative(start_x, start_y, maze):
    """
    Gera passagens no labirinto usando uma pilha para evitar recursão.
    """
    stack = [(start_x, start_y)]  # Inicializa a pilha com o ponto inicial
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Movimentos possíveis

    while stack:
        cx, cy = stack.pop()  # Remove a célula do topo da pilha
        random.shuffle(directions)  # Embaralha as direções para aleatoriedade

        for dx, dy in directions:
            nx, ny = cx + dx * 2, cy + dy * 2  # Próxima posição
            # Verifica se a nova posição está dentro dos limites e é uma parede
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 1:
                # Remove a parede intermediária
                maze[cy + dy][cx + dx] = 0
                # Abre a próxima célula
                maze[ny][nx] = 0
                # Adiciona a nova posição à pilha
                stack.append((nx, ny))

def generate_maze(width, height):
    """
    Gera um labirinto iterativamente.
    """
    # Inicializa o labirinto com todas as células como paredes
    maze = [[1 for _ in range(width)] for _ in range(height)]
    maze[1][1] = 0  # Define o ponto inicial como caminho
    # Chama a função iterativa para gerar as passagens
    carve_passages_iterative(1, 1, maze)
    return maze  # Retorna o labirinto gerado
