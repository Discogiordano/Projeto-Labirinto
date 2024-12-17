from maze_generator import generate_maze
from maze_solver import solve_maze
from maze_agent import move_agent

def main():
    width, height = 21, 21  # Dimensões do labirinto
    maze = generate_maze(width, height)  # Gera o labirinto
    path = solve_maze(maze)  # Resolve o labirinto
    move_agent(maze, path)  # Move o agente pelo labirinto

if __name__ == "__main__":
    main()
