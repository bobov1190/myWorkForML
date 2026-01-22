# ### 1
# edges_num = input("Enter number of edges: ") # Нам сначала нужно узнать размер матрицы смежности

# adjacency_matrix = [] # Инициализируем пустую матрицу смежности
# print("Enter adjacency matrix row by row (space-separated values):")

# for _ in range(int(edges_num)): # Считываем матрицу смежности построчно
#     row_str = input().split() # Считываем строку и разбиваем её на элементы
#     adjacency_matrix.append([int(x) for x in row_str]) # Преобразуем элементы в целые числа и добавляем в матрицу

# for i in range(int(edges_num)):
#     for j in range(int(edges_num)):
#         if i == j and adjacency_matrix[i][j] == 1:
#             print(i)
# else:
#     print("NO LOOPS")


# professional solution

import sys


# adjacency_matrix = []
# first_row = sys.stdin.readline().split()
# adjacency_matrix.append([int(x) for x in first_row])
# n = len(first_row)

# for i in range(0, int(n)):
#     row = sys.stdin.readline().split()
#     adjacency_matrix.append([int(x) for x in row])

# loops = []
# for i in range(0, int(n)):
#     for j in range(0, int(n)):
#         if i == j and adjacency_matrix[i][j] == 1:
#             print(i)
#             loops.append(i)

# if len(loops) == 0:
#     print("NO LOOPS")


### 2

# adjacency_matrix = []
# first_row = sys.stdin.readline().split()
# adjacency_matrix.append([int(x) for x in first_row])
# n = len(first_row)

# for i in range(n-1):
#     row = sys.stdin.readline().split()
#     if len(row) == 0:
#         break
#     adjacency_matrix.append([int(x) for x in row])

# row = []

# for i in range(n):

#     if sum(adjacency_matrix[i]) == 0:
#         print(f"")
#     else: 
#         list = []
        
#         for j in range(n):
#             if adjacency_matrix[i][j] == 1:
#                 list.append(str(j))
#         print(" ".join(list))


### 3

# edges_num = input("Enter number of edges: ") # Нам сначала нужно узнать размер матрицы смежности

# adjacency_matrix = [] # Инициализируем пустую матрицу смежности
# print("Enter adjacency matrix row by row (space-separated values):")

# num_edges = []
# for _ in range(int(edges_num)): # Считываем матрицу смежности построчно
#     num_edge = input()
#     num_edges.append(int(num_edge))

# print(num_edges)

# for i in range(int(edges_num)):

# N = int(input())

# matrix = [[0] * N for _ in range(N)]

# for i in range(N):
#     neighbors = sys.stdin.readline().split()
#     for neighbor in neighbors:
#         j = int(neighbor)
#         matrix[i][j] = 1 # Ставим связь из i в j

# for row in matrix:
#     print(" ".join(map(str, row)))


N = int(input())
adjacency_matrix = [] # Инициализируем пустую матрицу смежности

for _ in range(int(N)):
    row_str = input().split()
    adjacency_matrix.append([int(x) for x in row_str])

neighbors = input().split()
start_node = int(neighbors[0])
end_node = int(neighbors[1])


# ... unfinished


import sys
from collections import deque

def main():
    # 1. Считываем N (количество вершин)
    line = sys.stdin.readline().strip()
    if not line:
        return
    n = int(line)

    # 2. Считываем матрицу смежности (N строк)
    adjacency_matrix = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        adjacency_matrix.append(row)

    # 3. Считываем S (старт) и T (финиш)
    # Они находятся в самой последней строке
    last_line = sys.stdin.readline().split()
    if not last_line:
        return
    start_node = int(last_line[0])
    end_node = int(last_line[1])

    # --- АЛГОРИТМ BFS (Поиск в ширину) ---
    
    # Очередь хранит пары (текущая_вершина, расстояние_от_старта)
    queue = deque([(start_node, 0)])
    
    # Множество для хранения уже посещенных вершин
    visited = {start_node}

    while queue:
        current, dist = queue.popleft() # Берем первого из очереди

        # Если мы дошли до цели, выводим ответ и выходим
        if current == end_node:
            print(dist)
            return

        # Проверяем всех соседей текущей вершины
        for neighbor in range(n):
            # Если в матрице стоит 1 и мы там еще не были
            if adjacency_matrix[current][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    # Если очередь опустела, а мы не нашли цель — пути нет
    print("-1")

if __name__ == "__main__":
    main()