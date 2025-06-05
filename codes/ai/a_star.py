import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g

        if current in visited:
            continue
        visited.add(current)

        for neighbour, cost in graph.get(current, []):
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(open_list, (new_f, new_g, neighbour, path + [neighbour]))

    return None, float('inf')

# ---------- Taking Input from User ----------

graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("\nEnter node name: ")
    neighbours = input("Enter neighbours and cost as (neighbour,cost) separated by space: ")
    if neighbours:
        graph[node] = [tuple(x.split(',')) for x in neighbours.split()]
        graph[node] = [(neigh, int(cost)) for neigh, cost in graph[node]]
    else:
        graph[node] = []

heuristic = {}
print("\nEnter heuristic values:")
for node in graph:
    heuristic[node] = int(input(f"Heuristic value for {node}: "))

start_node = input("\nEnter start node: ")
goal_node = input("Enter goal node: ")

# ---------- Run A* ----------
path, cost = a_star(graph, start_node, goal_node, heuristic)

if path:
    print("\nShortest path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found.")




# Enter number of nodes in the graph: 6
# Enter node name: A
# Enter neighbours of A (format: B,2 C,3): B,1 C,3
# Enter node name: B
# Enter neighbours of B (format: B,2 C,3): D,4 E,2
# Enter node name: C
# Enter neighbours of C (format: B,2 C,3): E,1
# Enter node name: D
# Enter neighbours of D (format: B,2 C,3): 
# Enter node name: E
# Enter neighbours of E (format: B,2 C,3): F,2
# Enter node name: F
# Enter neighbours of F (format: B,2 C,3): 
# Enter heuristic value for node A: 5
# Enter heuristic value for node B: 4
# Enter heuristic value for node C: 2
# Enter heuristic value for node D: 6
# Enter heuristic value for node E: 1
# Enter heuristic value for node F: 0
# Enter start node: A
# Enter goal node: F