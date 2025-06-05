# Take number of colors from user
max_colors = int(input("Enter the number of colors to use for graph coloring: "))

# Take number of edges
num_edges = int(input("Enter the number of edges: "))

# Build the graph as an adjacency list
graph = {}
for _ in range(num_edges):
    node1, node2 = map(int, input().split())  # Example: 0 1
    if node1 not in graph:
        graph[node1] = []
    graph[node1].append(node2)

    if node2 not in graph:
        graph[node2] = []
    graph[node2].append(node1)

# Get number of vertices from the graph
num_vertices = len(graph.keys())

# Predefined list of color names
color_names = ["red", "green", "violet", "blue", "yellow", "orange", "indigo"]

# Check if a color can be assigned to a node
def is_color_valid(graph, color_index, current_node, color_assignment):
    for neighbor in graph[current_node]:
        if color_assignment[neighbor] == color_names[color_index]:
            return False
    return True

# Backtracking function to try coloring the graph
def solve_graph_coloring(graph, max_colors, current_node, num_vertices, color_assignment):
    if current_node == num_vertices:
        return True

    for color_index in range(max_colors):
        if is_color_valid(graph, color_index, current_node, color_assignment):
            color_assignment[current_node] = color_names[color_index]
            if solve_graph_coloring(graph, max_colors, current_node + 1, num_vertices, color_assignment):
                return True
            color_assignment[current_node] = -1  # Backtrack

    return False

# Initialize the color assignment dictionary
color_assignment = {}
for node in graph.keys():
    color_assignment[node] = -1

print("Graph (Adjacency List):", graph)

# Start coloring from node 0
if solve_graph_coloring(graph, max_colors, 0, num_vertices, color_assignment):
    print("\n✅ Graph Colored Successfully:")
    for node, color in color_assignment.items():
        print(f"Node {node} --> {color}")
else:
    print(f"\n Cannot color the graph with {max_colors} colors.")







# Enter the number of colors to use for graph coloring: 3
# Enter the number of edges: 6
# 0 1
# 0 2
# 0 3
# 1 2
# 2 3
# 3 4













# def greedy_coloring(graph, max_colors):
#     color = {}

#     for node in graph:
#         used_colors = set()
#         for neighbor in graph[node]:
#             if neighbor in color:
#                 used_colors.add(color[neighbor])
        
#         assigned = False
#         for c in range(max_colors):
#             if c not in used_colors:
#                 color[node] = c
#                 assigned = True
#                 break
        
#         if not assigned:
#             color[node] = None  # Could not assign color

#     return color


# def take_graph_input():
#     graph = {}
#     n = int(input("Enter number of vertices: "))
#     for i in range(n):
#         edges = input(f"Enter space-separated neighbors of vertex {i}: ").split()
#         graph[i] = [int(x) for x in edges]
#     return graph


# #  Get graph and color limit from user
# graph = take_graph_input()
# max_colors = int(input("Enter the maximum number of colors allowed: "))

# #  Color the graph
# coloring = greedy_coloring(graph, max_colors)

# #  Print results
# print("\nGraph Coloring Result:")
# for node in range(len(graph)):
#     if coloring[node] is not None:
#         print(f"Vertex {node} ---> Color {coloring[node]} [Colored]")
#     else:
#         print(f"Vertex {node} ---> [Not Colored] ---> (Not enough colors)")


