class GraphMatrix:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0]*vertices for _ in range(vertices)]
    def add_edge(self,u,v,weight):
        self.graph[u][v]= weight
        self.graph[v][u]=weight
    def display(self):
        for row in self.graph:
            print(row)
g=GraphMatrix(4)
g.add_edge(0,1,2)
g.add_edge(0,2,4)
g.add_edge(1,2,5)
g.add_edge(2,3,8)
g.display()
                    