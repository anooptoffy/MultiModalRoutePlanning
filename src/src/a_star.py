from pygraph.classes.graph import graph
import pygraphviz as pgv

g = { "a" : ["d", "f"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["d"]
    }


G = graph()
G.add_node('a',attrs=['263P'])
G.add_node('d',attrs=['263P'])
G.add_edge(('a','d'),wt=1,label='263P')