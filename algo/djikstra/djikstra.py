import graphviz
import os
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'

depart = ""
dot = graphviz.Digraph(comment='Graph')

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
    dot.edge(i,j, label=str(graph[i][j]))
  

dot.render('graph_output', format='png', cleanup=True)

class Graph:
  def __init__(self, graph: dict = {}):
    self.graph = graph
    
  def add_edge(self, node1, node2, weight):
    self.graph[node1][node2] = weight
    
Graph.add_edge("A", "B", 5)
    