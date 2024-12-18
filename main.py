from maze_generator import generate_maze
from maze_interface import MazeApp
from labirinto_utils import load_labirinto, save_labirinto
import tkinter as tk

def main():
    """
    Função principal para executar o programa.
    """
    width, height = 21, 21  # Dimensões do labirinto

    # Tenta carregar o labirinto salvo
    maze = load_labirinto()
    if maze is None:
        print("Gerando novo labirinto fixo...")
        maze = generate_maze(width, height)
        save_labirinto(maze)  # Salva o labirinto para futuras execuções

    # Inicializa a interface gráfica
    root = tk.Tk()
    root.title("Labirinto - Agente com Aprendizado")
    app = MazeApp(root, maze)
    root.mainloop()

if __name__ == "__main__":
    main()
