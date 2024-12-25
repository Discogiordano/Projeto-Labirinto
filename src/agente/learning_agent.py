from src.agente.amostragem_utils import save_amostragem, load_amostragem

class LearningAgent:
    def __init__(self, canvas, cell_size, start, maze):
        """
        Inicializa o agente com lógica DFS e aprendizado usando amostragem.json.
        """
        self.canvas = canvas
        self.cell_size = cell_size
        self.start = start  # Posição inicial do agente
        self.maze = maze
        self.amostragem = load_amostragem()  # Carrega a amostragem do arquivo
        self.visited = set()  # Células visitadas nesta execução
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Movimentos possíveis
        self.agent_visual = None  # Representação gráfica do agente

    def dfs(self):
        """
        Implementa a lógica de DFS com aprendizado baseado na tabela amostragem.json.
        """
        stack = [self.start]  # Pilha para DFS
        path = []

        while stack:
            state = stack[-1]  # Pega o estado atual no topo da pilha

            # Verifica se o agente chegou ao objetivo
            if self.is_goal(state):
                print("Linha de chegada alcançada!")
                save_amostragem(self.amostragem)
                return True

            # Marca o estado como visitado
            if state not in self.visited:
                self.visited.add(state)  # Adiciona à lista de visitados
                path.append(state)  # Salva no caminho atual

            # Obtém as ações válidas a partir do estado atual
            valid_actions = self.get_valid_actions(state)

            if valid_actions:
                # Escolhe a melhor ação com base na amostragem
                action = self.choose_action(state, valid_actions)
                next_state = (state[0] + action[0], state[1] + action[1])

                # Move o agente graficamente
                self.move_agent(state, next_state)

                # Adiciona o próximo estado à pilha
                stack.append(next_state)
            else:
                print(f"Beco sem saída na célula {state}. Retornando para o estado anterior.")
                self.register_error(state)
                save_amostragem(self.amostragem)
                stack.pop()
                if stack:
                    previous_state = stack[-1]
                    # Anima o movimento de retorno
                    self.move_agent(state, previous_state)


        print("Caminho sem solução!")
        save_amostragem(self.amostragem)
        return False

    def get_valid_actions(self, state):
        """
        Retorna as ações válidas a partir do estado atual, considerando o labirinto e visitas.
        """
        return [
            action for action in self.directions
            if self.is_valid((state[0] + action[0], state[1] + action[1]))
        ]

    def choose_action(self, state, valid_actions):
        """
        Escolhe a melhor ação com base na tabela amostragem.json.
        """
        best_action = None
        best_score = float("inf")  # Queremos o menor "peso" ou penalidade

        for action in valid_actions:
            next_state = (state[0] + action[0], state[1] + action[1])
            score = 0 

            # Penaliza células marcadas como becos sem saída
            if str(next_state) in self.amostragem["errors"]:
                score += 100  # Penalidade alta para erros

            if score < best_score:
                best_score = score
                best_action = action

        return best_action

    def register_error(self, state):
        """
        Registra um beco sem saída na tabela amostragem.
        """
        state_key = str(state)
        if state_key not in self.amostragem["errors"]:
            self.amostragem["errors"].append(state_key)

    def is_goal(self, state):
        """
        Verifica se o estado atual é a linha de chegada.
        """
        return state == (len(self.maze[0]) - 2, len(self.maze) - 2)

    def is_valid(self, state):
        """
        Verifica se o estado é válido (não é parede e está dentro dos limites).
        """
        x, y = state
        return (0 <= x < len(self.maze[0]) and
                0 <= y < len(self.maze) and
                self.maze[y][x] == 0 and
                state not in self.visited and
                str(state) not in self.amostragem["errors"])

    def move_agent(self, current_state, next_state):
        """
        Move o agente graficamente de uma célula para outra.
        """
        cx, cy = current_state
        nx, ny = next_state

        # Apaga o agente na célula atual
        if self.agent_visual:
            self.canvas.delete(self.agent_visual)

        # Desenha o agente na nova célula
        self.agent_visual = self.canvas.create_rectangle(
            nx * self.cell_size, ny * self.cell_size,
            (nx + 1) * self.cell_size, (ny + 1) * self.cell_size,
            fill="blue", outline="gray"
        )
        self.canvas.update()
        self.canvas.after(100)
