import json

def load_amostragem(file_path="amostragem.json"):
    """
    Carrega o arquivo de amostragem contendo os dados do labirinto.
    Se o arquivo não existir, retorna uma estrutura inicial vazia.
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"visited": {}, "errors": []}

def save_amostragem(data, file_path="amostragem.json"):
    """
    Salva os dados de amostragem no arquivo.
    """
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
