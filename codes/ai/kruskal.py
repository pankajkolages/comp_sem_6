# Disjoint Set (Union-Find) Helper Functions
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v
            return True
        return False

# Kruskal's Algorithm
def kruskal(vertices, edges):
    mst = []
    ds = DisjointSet(vertices)

    # Sort all edges by weight (ascending)
    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))

    return mst

# ---------- User Input ----------
print("Kruskal's MST Algorithm")
n = int(input("Enter number of vertices: "))
vertices = input("Enter vertex labels (space-separated): ").split()

e = int(input("Enter number of edges: "))
edges = []
print("Enter edges in format: u v weight")
for _ in range(e):
    u, v, w = input().split()
    edges.append((u, v, int(w)))

# ---------- Run Kruskal ----------
mst = kruskal(vertices, edges)

# ---------- Output ----------
print("\nMinimum Spanning Tree edges:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")


# Enter number of vertices: 
# 4
# Enter vertex labels (space-separated): 
# A B C D
# Enter number of edges: 
# 5
# Enter edges in format: u v weight
# A B 1
# A C 5
# B C 3
# B D 4
# C D 2