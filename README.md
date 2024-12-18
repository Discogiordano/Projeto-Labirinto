# Labirinto - Agente com DFS

🧩 **Descrição**

Este projeto implementa um agente que navega por um labirinto utilizando o algoritmo **DFS (Depth-First Search)**. O agente tenta explorar todas as opções possíveis até encontrar a solução. Durante a exploração, o agente registra os estados visitados e os becos sem saída, criando uma tabela de amostragem que ajuda a evitar ciclos e otimizar o caminho.

🧠 **Objetivo**

O objetivo do agente é alcançar a linha de chegada do labirinto, utilizando o algoritmo de **Busca em Profundidade (DFS)**, e registrar suas ações para otimizar futuras tentativas.

📑 **Funcionalidades**

- Geração automática de labirinto.
- Implementação do algoritmo DFS para exploração do labirinto.
- Registro de estados visitados e erros em um arquivo JSON.
- Representação gráfica da exploração do labirinto.

🔧 **Tecnologias Utilizadas**

- **Python**: Linguagem de programação principal.
- **Tkinter**: Biblioteca para a criação da interface gráfica do labirinto.
- **JSON**: Para salvar as amostragens e estados visitados durante a exploração.

📚 **Como Usar**

1. **Instalar Dependências**:  
   Para instalar as dependências, basta rodar o comando abaixo:

   ```bash
   pip install -r requirements.txt

2. **Eexecutar o programa**:  
   ```bash
   python main.py
