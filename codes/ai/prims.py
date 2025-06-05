import heapq

def prims_algo(graph, start):
    visited = set()
    min_heap = []
    mst_edges = []
    total_cost = 0

    for neighbour, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbour))
    
    visited.add(start)

    while min_heap:
        weight, from_node, to_node = heapq.heappop(min_heap)

        if to_node not in visited:
            visited.add(to_node)
            mst_edges.append((from_node, to_node, weight))
            total_cost += weight

            for neighbour, edge_weight in graph[to_node]:
                if neighbour not in visited:
                    heapq.heappush(min_heap, (edge_weight, to_node, neighbour))
                
    return mst_edges, total_cost

# -------- User Input --------
graph = {}
num_edges = int(input("Enter number of edges: "))

print("Enter edges in format: <node1> <node2> <weight>")
for _ in range(num_edges):
    u, v, w = input().split()
    w = int(w)

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    # Since undirected graph
    graph[u].append((v, w))
    graph[v].append((u, w))

start_node = input("Enter starting node: ")

# -------- Run Prim's Algorithm --------
mst, cost = prims_algo(graph, start_node)

print("\nEdges in MST from Prim's Algorithm:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} (weight: {edge[2]})")

print("\nTotal Cost:", cost)







# Enter number of edges: 5
# Enter edges in format: <node1> <node2> <weight>
# A B 1
# A C 3
# A D 4
# B C 2
# C D 5
# Enter starting node: A
