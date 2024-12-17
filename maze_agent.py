import os
import time

def display_maze_with_agent(maze, path, agent_position=None):
    if agent_position is None:
        agent_position = path[0]
    
    os.system("cls" if os.name == "nt" else "clear")
    for y, row in enumerate(maze):
        line = ""
        for x, cell in enumerate(row):
            if (x, y) == agent_position:
                line += "🤖"  # Agente
            elif (x, y) in path:
                line += "🟩"  # Caminho
            elif cell == 1:
                line += "⬛"  # Parede
            else:
                line += "⬜"  # Caminho vazio
        print(line)

def move_agent(maze, path):
    for position in path:
        display_maze_with_agent(maze, path, agent_position=position)
        time.sleep(0.2)
