import pygraph
from pygraph.classes.graph import graph
from pygraph.algorithms.heuristics.euclidean import euclidean
from pygraph.algorithms.heuristics.chow import chow
from pygraph.classes import exceptions
from pygraph.algorithms.minmax import minimal_spanning_tree,\
shortest_path, heuristic_search, shortest_path_bellman_ford, maximum_flow, cut_tree
import pygraphviz
import os
import csv
import random
import pickle
from math import radians, cos, sin, asin, sqrt, inf
from collections import OrderedDict

heuristic = pickle.load(open("data/heuristic.json",'rb'))
G = pickle.load(open("data/graph.json", "rb"))

# result = pygraph.algorithms.minmax.heuristic_search(G,'8th mile t dasarahalli 8th mile beside a.k.scooter works','madanayakanahalli madanayakanahalli beside usha bakery and sweets', heuristic)
# print(result)

result = pygraph.algorithms.minmax.heuristic_search(G,'8th mile t dasarahalli 8th mile beside a.k.scooter works','byadarahalli', heuristic)
print(result)