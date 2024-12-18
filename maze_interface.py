import tkinter as tk
from amostragem_utils import load_amostragem
from learning_agent import LearningAgent

class MazeApp:
    def __init__(self, root, maze):
        """
        Inicializa a interface gráfica com o agente DFS.
        """
        self.root = root
        self.maze = maze
        self.cell_size = 20
        self.canvas = tk.Canvas(
            root, 
            width=len(maze[0]) * self.cell_size, 
            height=len(maze) * self.cell_size
        )
        self.canvas.pack()

        # Carrega a amostragem
        self.amostragem = load_amostragem()

        # Inicializa o agente
        self.agent = LearningAgent(self.canvas, self.cell_size, (1, 1), maze, self.amostragem)
        self.draw_maze()
        self.agent.draw()

        # Inicia o DFS
        if not self.agent.dfs():
            print("Execução finalizada sem sucesso.")

    def draw_maze(self):
        """
        Desenha o labirinto na interface gráfica.
        """
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                color = "black" if cell == 1 else "white"
                self.canvas.create_rectangle(
                    x * self.cell_size, y * self.cell_size,
                    (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                    fill=color, outline="gray"
                )
