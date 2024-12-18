import json

def load_labirinto(file_path="labirinto.json"):
    """
    Carrega o labirinto salvo de um arquivo.
    Se não existir, retorna None.
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def save_labirinto(maze, file_path="labirinto.json"):
    """
    Salva o labirinto em um arquivo.
    """
    with open(file_path, "w") as file:
        json.dump(maze, file, indent=4)
