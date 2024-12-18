import tkinter as tk  # Importa Tkinter para a interface gráfica

class MazeApp:
    def __init__(self, root, maze, path):
        """
        Inicializa a interface gráfica do labirinto e movimentação do agente.
        """
        self.root = root
        self.maze = maze
        self.path = path
        self.cell_size = 10  # Define o tamanho de cada célula
        self.canvas = tk.Canvas(
            root, 
            width=len(maze[0]) * self.cell_size, 
            height=len(maze) * self.cell_size
        )
        self.canvas.pack()
        self.agent_position = path[0]  # Posição inicial do agente
        self.draw_maze()  # Desenha o labirinto na interface
        self.draw_finish_line()  # Marca a célula de chegada
        self.move_agent()  # Inicia o movimento do agente

    def draw_maze(self):
        """
        Desenha o labirinto na tela.
        """
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                color = "black" if cell == 1 else "white"  # Define cor (parede ou caminho)
                self.canvas.create_rectangle(
                    x * self.cell_size, y * self.cell_size,
                    (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                    fill=color, outline="gray"
                )

    def draw_finish_line(self):
        """
        Marca a célula de linha de chegada com a cor vermelha.
        """
        end_x, end_y = self.path[-1]  # Obtém as coordenadas da célula final
        self.canvas.create_rectangle(
            end_x * self.cell_size, end_y * self.cell_size,
            (end_x + 1) * self.cell_size, (end_y + 1) * self.cell_size,
            fill="red", outline="gray"
        )

    def move_agent(self):
        """
        Move o agente ao longo do caminho encontrado.
        """
        for position in self.path:
            x, y = position
            # Desenha o agente na nova posição
            self.canvas.create_rectangle(
                x * self.cell_size, y * self.cell_size,
                (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                fill="blue", outline="gray"
            )
            self.root.update()  # Atualiza a interface
            self.root.after(100)  # Pausa para criar a animação
        print("O agente chegou ao final do labirinto!")
