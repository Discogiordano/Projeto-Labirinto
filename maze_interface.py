import tkinter as tk
from learning_agent import LearningAgent

class MazeApp:
    def __init__(self, root, maze):
        """
        Inicializa a interface gráfica com o agente DFS.
        """
        self.root = root
        self.maze = maze
        self.cell_size = 20  # Tamanho de cada célula
        self.canvas = tk.Canvas(
            root, 
            width=len(maze[0]) * self.cell_size, 
            height=len(maze) * self.cell_size
        )
        self.canvas.pack()

        # Inicializa o agente DFS
        self.agent = LearningAgent(
            canvas=self.canvas,
            cell_size=self.cell_size,
            start=(1, 1),  # Posição inicial do agente
            maze=self.maze
        )

        # Desenha o labirinto na interface gráfica
        self.draw_maze()

        # Inicia o movimento do agente
        self.agent.dfs()

    def draw_maze(self):
        """
        Desenha o labirinto na interface gráfica.
        """
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                color = "black" if cell == 1 else "white"  # Preto para paredes, branco para caminhos
                self.canvas.create_rectangle(
                    x * self.cell_size, y * self.cell_size,
                    (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                    fill=color, outline="gray"
                )
