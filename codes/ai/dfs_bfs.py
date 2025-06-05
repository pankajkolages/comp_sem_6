from collections import deque

# Function to take user input for the graph
def input_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node name: ").strip()
        neighbours = input(f"Enter neighbours of {node} separated by space: ").strip().split()
        graph[node] = neighbours
    return graph

# DFS Function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbour in graph.get(start, []):
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbour in graph.get(vertex, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Main code
graph = input_graph()
start_node = input("Enter starting node for traversal: ").strip()

print("\nDFS Traversal:")
dfs(graph, start_node)
print("\n\nBFS Traversal:")
bfs(graph, start_node)









# Enter number of nodes: 6
# Enter node name: A
# Enter neighbours of A separated by space: B C
# Enter node name: B
# Enter neighbours of B separated by space: A D E
# Enter node name: C
# Enter neighbours of C separated by space: A F
# Enter node name: D
# Enter neighbours of D separated by space: B
# Enter node name: E
# Enter neighbours of E separated by space: B
# Enter node name: F
# Enter neighbours of F separated by space: C
# Enter starting node for traversal: A







































# from collections import deque

# # Input function to build the graph
# def input_graph():
#     n = int(input("Enter total number of node elements: "))
#     graph = {}
#     for _ in range(n):
#         node = input("Enter node element: ").strip()
#         neighbours = input(f"Enter neighbours of node {node} separated by space in format (a b): ").strip().split()
#         graph[node] = neighbours
#     return graph

# # DFS for a connected component
# def dfs(graph, start, visited):
#     visited.add(start)
#     print(start, end=' ')
#     for neighbour in graph[start]:
#         if neighbour not in visited:
#             dfs(graph, neighbour, visited)

# # Full DFS traversal covering disconnected components
# def full_dfs(graph):
#     visited = set()
#     print("Full DFS traversal:")
#     for node in graph:
#         if node not in visited:
#             dfs(graph, node, visited)
#     print()

# # BFS for a connected component
# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited.add(start)
#     while queue:
#         vertex = queue.popleft()
#         print(vertex, end=' ')
#         for neighbour in graph[vertex]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# # Full BFS traversal covering disconnected components
# def full_bfs(graph):
#     visited = set()
#     print("Full BFS traversal:")
#     for node in graph:
#         if node not in visited:
#             bfs(graph, node, visited)
#     print()

# # Main program
# graph = input_graph()
# start_node = input("Enter start node for DFS and BFS: ").strip()

# print("\nDFS traversal from", start_node, ":")
# dfs(graph, start_node, set())
# print("\nBFS traversal from", start_node, ":")
# bfs(graph, start_node, set())

# print()
# full_dfs(graph)
# full_bfs(graph)


