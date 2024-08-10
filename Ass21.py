class Graph:
    def __init__(self,no_of_vertex):
        self.vertex_count=no_of_vertex
        self.adj_matrix=[[0]*no_of_vertex  for i in range(no_of_vertex) ]

    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("Invalid...")

    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("Invalid...")

    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix!=0
        else:
            print("Invalid...")
            return False

    def print_adj_matrix(self):
        for i in self.adj_matrix:
            print(" ".join(map(str,i)))

g1 = Graph(5)
g1.add_edge(0,1)
g1.add_edge(1,2)
g1.add_edge(1,3)
print("(1,2) has an edge :",g1.has_edge(1,2))
g1.add_edge(2,3)
g1.add_edge(3,4)

g1.print_adj_matrix()