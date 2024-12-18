from amostragem_utils import save_amostragem

class LearningAgent:
    def __init__(self, canvas, cell_size, start, maze, amostragem):
        """
        Inicializa o agente com lógica DFS.
        """
        self.canvas = canvas
        self.cell_size = cell_size
        self.start = start  # Posição inicial do agente
        self.position = start
        self.maze = maze
        self.amostragem = amostragem  # Dados persistentes de amostragem
        self.visited = set()  # Células visitadas nesta execução
        self.visual = None  # Representação gráfica do agente
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Movimentos possíveis

    def draw(self):
        """
        Desenha o agente na posição inicial.
        """
        x, y = self.position
        self.visual = self.canvas.create_rectangle(
            x * self.cell_size, y * self.cell_size,
            (x + 1) * self.cell_size, (y + 1) * self.cell_size,
            fill="blue", outline="gray"
        )

    def dfs(self):
        """
        Implementa a lógica de DFS para o agente explorar o labirinto.
        Retorna True se encontrar a linha de chegada, ou False se falhar.
        """
        stack = [self.start]  # Inicializa a pilha com a posição inicial
        path = []  # Caminho atual

        while stack:
            cx, cy = stack[-1]  # Pega a célula no topo da pilha sem removê-la
            path.append((cx, cy))

            # Verifica se a célula já foi visitada na execução atual
            if (cx, cy) in self.visited:
                print(f"Repetiu a célula {cx, cy} na mesma execução. Finalizando.")
                self.amostragem["errors"].append({"path": path, "reason": "Repeated cell"})
                save_amostragem(self.amostragem)
                return False
            self.visited.add((cx, cy))  # Marca a célula como visitada na execução atual

            # Atualiza a amostragem global (para execuções futuras)
            cell_str = str((cx, cy))
            self.amostragem["visited"][cell_str] = self.amostragem["visited"].get(cell_str, 0) + 1

            # Desenha o agente na posição atual
            self.canvas.create_rectangle(
                cx * self.cell_size, cy * self.cell_size,
                (cx + 1) * self.cell_size, (cy + 1) * self.cell_size,
                fill="blue", outline="gray"
            )
            self.canvas.update()
            self.canvas.after(100)

            # Verifica se é a célula final (linha de chegada)
            if self.is_goal(cx, cy):
                print("Linha de chegada alcançada!")
                save_amostragem(self.amostragem)
                return True

            # Encontra vizinhos válidos
            found_valid_move = False
            for dx, dy in self.directions:
                nx, ny = cx + dx, cy + dy
                if self.is_valid(nx, ny):
                    stack.append((nx, ny))  # Adiciona o vizinho à pilha
                    found_valid_move = True
                    break

            # Se nenhum vizinho válido foi encontrado, remove a célula atual da pilha
            if not found_valid_move:
                stack.pop()  # Beco sem saída, volta para a célula anterior

        return False

    def is_goal(self, x, y):
        """
        Verifica se a célula atual é a linha de chegada.
        """
        return (x, y) == (len(self.maze[0]) - 2, len(self.maze) - 2)  # Posição final padrão

    def is_valid(self, x, y):
        """
        Verifica se a célula é válida para exploração.
        """
        return (0 <= x < len(self.maze[0]) and 0 <= y < len(self.maze) and
                self.maze[y][x] == 0 and (x, y) not in self.visited)
