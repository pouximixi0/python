#import graphviz
import os
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'

depart = ""
#dot = graphviz.Digraph(comment='Graph')

graph = {
  "Paris": {"Rennes": 1, "Tours": 1, "Lille": 1, "Nancy": 1},
  "Marseille": {"Toulouse": 1, "Lyon": 1},
  "Lyon": {"Clermont-Ferrand": 1, "Nancy": 1},
  "Nancy": {"Strasbourg": 1 , "Paris": 1},
  "Strasbourg": {"Nancy": 1},
  "Lille": {"Paris": 1},
  "Toulouse": {"Bordeaux": 1},
  "Nice": {"Toulouse": 1},
  "Rennes": {"Paris": 1, "Tours": 1},
  "Tours": {"Paris": 1, "Clermont-Ferrand": 1, "Rennes": 1},
  "Clermont-Ferrand": {"Lyon": 1, "Bordeaux": 1, "Tours": 1},
  "Bordeaux": {"Clermond-Ferrand": 1, "Toulouse": 1},
  
}

for i in graph:
  for j in graph[i]:
    #dot.edge(i,j, label=str(graph[i][j]))
    pass
  

#dot.render('graph_output', format='png', cleanup=True)

def djikstra(graph, start):
  distance = {}
  finished = True
  lowest_node = None
  for i in graph:
    distance[i] = float('inf')
    distance[start] = 0
    
  while finished:
    
    for i in graph:
      print(lowest_node)
      lowest_node = None
      lowest = float('inf')
      print(i)
      if i == start:
        for j in graph[i]:
          if float(graph[i][j]) < lowest:
            lowest = float(graph[i][j])
            lowest_node = j
        distance[lowest_node] = graph[i][lowest_node]
    print(distance)
    finished = False
class Graph:
  def __init__(self, graph: dict = {}):
    self.graph = graph
    
  def add_edge(self, node1, node2, weight):
    if node1 not in self.graph:
      self.graph[node1] = {}
    self.graph[node1][node2] = weight
    
    if node2 not in self.graph:
      self.graph[node2] = {}
    self.graph[node2][node1] = weight
    
G = Graph()
G.add_edge("A", "B", 16)
G.add_edge("B", "E", 5)
G.add_edge("E", "F", 2)
G.add_edge("F", "D", 12)
G.add_edge("D", "B", 4)
G.add_edge("D", "C", 30)


djikstra(G.graph, 'E')


"""
flowchart LR

A((A))
B((B))
C((C))
D((D))
E((E))
F((F))


A-.16.-B
B-.5.-E
E-.2.-F
F-.12.-D
D-.4.-B
D-.30.-C
"""
