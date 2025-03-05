import heapq
class GraphDijkstra :
    def __init__(self,vertices):
        self.V=vertices
        self.graph={i:[] for i in range(vertices)}
def add_edge(self, u, v, weight):
    self.graph[v].append((v, weight))
    self.graph[u].append((u, weight))

def dijkstra(self, src):
    heap= [(0, src)]
    distances ={i: float ('inf') for i in range(self.v)}
    distances [src]=0
    while heap:
        dist, node= heapq.heappop (heap)
        for neighbor, weight in self.graph [node] :
            new_dist=dist+ weight
            if new_dist <distances[neighbor]:
                distances[neighbor]= new_dist
                heapq.heappush (heap, (new_dist, neighbor))
    print(distances)
    

g=GraphDijkstra(4)
g.add_edge(0, 1, 2)
g.add_edge(1, 2, 4)
g.add_edge(1, 2, 5)
g.add_edge(2, 3, 8)
g.dijkstra(0)