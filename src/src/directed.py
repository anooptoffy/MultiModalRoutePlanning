import sys
from pygraph.dgraph import PyGraph

g = PyGraph()

g.add_relation('A likes B')
g.add_relation('A dislikes C')
g.add_relation('B loves C')
g.add_relation('C likes A')

g.draw_graph()