
import pygraph
from pygraph.classes.graph import graph
from pygraph.classes.digraph import digraph
from pygraph.algorithms.heuristics.euclidean import euclidean
from pygraph.algorithms.heuristics.chow import chow
from pygraph.classes import exceptions
from pygraph.algorithms.minmax import minimal_spanning_tree, \
    shortest_path, heuristic_search, shortest_path_bellman_ford, \
    maximum_flow, cut_tree
import pygraphviz
import os
import csv
import random
import pickle
from math import radians, cos, sin, asin, sqrt, inf
from collections import OrderedDict


g = pygraph.classes.graph .graph()
g.add_nodes(['A', 'B', 'C'])
g.add_node_attribute('A', ('position', (0, 0)))
g.add_node_attribute('B', ('position', (1, 1)))
g.add_node_attribute('C', ('position', (0, 2)))
g.add_edge(('A', 'B'), wt=2)
g.add_edge(('B', 'C'), wt=2)
g.add_edge(('A', 'C'), wt=4)
h = euclidean()
h.optimize(g)
result = pygraph.algorithms.minmax.heuristic_search(g,'A', 'C', h)
print(result)
