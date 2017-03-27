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


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians,
                                 [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(
        dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r

# creating a graph
G = pygraph.classes.graph.graph()

node_loc = pickle.load(open("data/bus_stops_loc.json", "rb"))
print(type(node_loc))

node_routes = pickle.load(open("data/bus_stops_routes_bmtc.json",
                               "rb"))
print(type(node_routes))



# Adding nodes to the graph
for key in node_loc.keys():
    G.add_node(key, attrs=[('position',[0,0]), ('location',
                                               node_loc[key]), ("routes",
                                                         node_routes[key])])

#print(G.nodes())
#print(G.node_attributes(' hampinagara 7th main vijayanagara beside mrudula medicals'))

# Adding edges
with open("../data/bmtc data/2.bus_stations.csv", 'rt',
          encoding='utf-8') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')
    prev_route = 0
    next_route = 1
    prev_stop = 0
    next_stop = 1
    for row in readfile:
        next_route = row[4]
        next_stop = row[3]
        if prev_route == next_route:
            long1 = float(node_loc[prev_stop][0])
            latit1 = float(node_loc[prev_stop][1])
            long2 = float(node_loc[next_stop][0])
            latit2 = float(node_loc[next_stop][1])
            wt = haversine(long1, latit1, long2, latit2)
            if not G.has_edge((prev_stop, next_stop)):
                G.add_edge((prev_stop, next_stop), wt=wt)
            prev_stop = row[3]
        else:
            prev_route = row[4]
            prev_stop = row[3]

heuristic = euclidean()
heuristic.optimize(G)
result = pygraph.algorithms.minmax.heuristic_search(G,'8th mile t dasarahalli 8th mile beside a.k.scooter works','madanayakanahalli madanayakanahalli beside usha bakery and sweets', heuristic)
print(result)