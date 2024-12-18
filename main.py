from maze_interface import MazeApp  # Importa a interface gráfica
from maze_generator import generate_maze  # Importa a função para gerar o labirinto
from maze_solver import solve_maze  # Importa a função para resolver o labirinto
import tkinter as tk  # Importa Tkinter para criar a interface gráfica

def main():
    """
    Função principal para integrar e executar o programa.
    """
    width, height = 61, 61 # Grandes dimensões do labirinto
    maze = generate_maze(width, height)  # Gera o labirinto
    path = solve_maze(maze)  # Resolve o labirinto e encontra o caminho

    # Inicializa a janela Tkinter
    root = tk.Tk()
    root.title("Labirinto - Interface Gráfica")
    # Cria a interface gráfica do labirinto
    app = MazeApp(root, maze, path)
    root.mainloop()  # Executa o loop principal da interface gráfica

if __name__ == "__main__":
    main()  # Executa a função principal
