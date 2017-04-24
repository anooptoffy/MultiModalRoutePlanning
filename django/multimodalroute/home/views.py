from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import SubmitForm

import pygraph
from pygraph.classes.graph import graph
from pygraph.classes.digraph import digraph
#from pygraph.algorithms.heuristics.euclidean import euclidean
#from pygraph.algorithms.heuristics.chow import chow
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
import time

class euclidean(object):
    """
    A* heuristic for Euclidean graphs.

    This heuristic has three requirements:
        1. All nodes should have the attribute 'position';
        2. The weight of all edges should be the euclidean distance
        between the nodes it links;
        3. The C{optimize()} method should be called before the
        heuristic search.

    A small example for clarification:
    """

    def __init__(self):
        """
        Initialize the heuristic object.
        """
        self.distances = {}

    def optimize(self, graph):
        """
        Build a dictionary mapping each pair of nodes to a number (
        the distance between them).

        @type  graph: graph
        @param graph: Graph.
        """
        for start in graph.nodes():
            for end in graph.nodes():
                for each in graph.node_attributes(start):
                    if (each[0] == 'position'):
                        start_attr = each[1]
                        break
                for each in graph.node_attributes(end):
                    if (each[0] == 'position'):
                        end_attr = each[1]
                        break
                dist = 0
                long1 = float(start_attr[0])
                latit1 = float(start_attr[1])
                long2 = float(end_attr[0])
                latit2 = float(end_attr[1])
                dis = haversine(long1, latit1, long2, latit2)

                self.distances[(start, end)] = dist

    def __call__(self, start, end):
        """
        Estimate how far start is from end.

        @type  start: node
        @param start: Start node.

        @type  end: node
        @param end: End node.
        """
        assert len(list(
            self.distances.keys())) > 0, "You need to optimize this " \
                                         "heuristic for your graph " \
                                         "before it can be used to " \
                                         "estimate."

        return self.distances[(start, end)]

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



def find_route(mypath):
    j=len(mypath)
    start = mypath[0]
    res=set(node_routes[start])
    i=1
    while i<j:
        n_res=set(node_routes[mypath[i]])&res
        if n_res:
            c=1
        else:
            stop=mypath[i-1]
            print (start+"      "+"->"+stop+":",res)
            print ("change bus")
            start=stop
            n_res=set(node_routes[start])
            i=i-1
        i+=1
        res = n_res
    stop=mypath[i-1]
    print (start + "->" + stop + ":", res)



def index(request):
    # creating a graph
    G = pygraph.classes.graph.graph()
    # G = pygraph.classes.digraph.digraph()

    # reading bus stops
    node_loc = pickle.load(open("home/static/home/bus_stops_loc.json",
                                "rb"))


    # reading metro info
    metro_loc = pickle.load(open(
        "home/static/home/metro_stops_loc.json","rb"))

    print(type(node_loc))

    node_routes = pickle.load(open(
        "home/static/home/bus_stops_routes_bmtc.json",
        "rb"))
    metro_routes = pickle.load(open(
        "home/static/home/metro_routes.json","rb"))

    print(type(node_routes))

    # Adding nodes to the graph
    for key in node_loc.keys():
        G.add_node(key, attrs=[('position', node_loc[key]), ("routes",
                                                             node_routes[
                                                                 key])])

    for key in metro_loc.keys():
        G.add_node(key, attrs=[('position', metro_loc[key]),
                               ("routes", metro_routes[key])])


    # Adding edges
    with open("home/static/home/2.bus_stations.csv", 'rt',
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


    with open("home/static/home/MetroStation.csv", 'rt', encoding=
    'utf-8') as csvfile:
        readfile = csv.reader(csvfile, delimiter=',')
        prev_route = 0
        next_route = 1
        prev_stop = 0
        next_stop = 1
        for row in readfile:
            next_route = row[4]
            next_stop = row[3]
            if prev_route ==  next_route:
                long1 = float(metro_loc[prev_stop][0])
                latit1 = float(metro_loc[prev_stop][1])
                long2 = float(metro_loc[next_stop][0])
                latit2 = float(metro_loc[next_stop][1])
                wt = haversine(long1, latit1, long2, latit2)
                if not G.has_edge((prev_stop, next_stop)):
                    G.add_edge((prev_stop, next_stop), wt= wt)
                prev_stop = row[3]
            else:
                prev_route = row[4]
                prev_stop = row[3]


    for key_metro in metro_loc.keys():
        for key_bus in node_loc.keys():
            wt = haversine(float(metro_loc[key_metro][0]),
                           float(metro_loc[key_metro][1]),
                           float(node_loc[key_bus][0]),
                           float(node_loc[key_bus][1]))
            if wt < 5.0:
                G.add_edge((key_metro, key_bus), wt= wt)



    if 'source' not in request.POST:
        form = SubmitForm()
        textMessage = "Form Not Submitted"
    else:
        form = SubmitForm()
        heuristic = euclidean()
        heuristic.optimize(G)

        # result = pygraph.algorithms.minmax.heuristic_search(G,'electronic city wipro gate','infosys parking lot', heuristic)
        result = pygraph.algorithms.minmax.heuristic_search(G,
        request.POST['source'],request.POST['destination'],
        heuristic)
        print(result)

        for r in range(len(result)):
            print(result[r]+"- "+", ".join(result[r]))

        textMessage  = '-> '.join(result)
        #find_route(result)

    return render(request, 'home/index.html', {'form' : form,
                                               'Message' : textMessage })










