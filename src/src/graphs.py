"""
A simple Python graph class.
http://www.python-course.eu/graphs_python.php
"""

class Graph:
    '''Python Graph Implementation
        Basic operations :
        1. Generate edges
        2. Isolated nodes
        3. vertices
        4. edges
        5. add_vertex
        6. add_edges
        7. find_paths
        8. find_all_paths
        9. vertex_degree
    '''
    def __init__(self, graph_dict = None):
        ''' Initializes the graph with graph dictionary / adjacency list representation
            if No graph dictionary is given initializes it with None
            or with the given graph_dict
        '''
        if graph_dict == None:
            self.__graph_dict = {}
        else:
            self.__graph_dict = graph_dict


    def __generate_edges(self):
        ''' returns a list of edges in the graphs'''
        edges = []
        for node in self.__graph_dict:
            for neighbour in self.__graph_dict[node]:
                edges.append((node, neighbour))

        return edges

    def isolated_nodes(self):
        isolated_nodes = []
        for node in self.__graph_dict:
            if not self.__graph_dict[node]:
                isolated_nodes += node
        return isolated_nodes

    def vertices(self):
        '''returns the list of vertices'''
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self,vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edges(self,edge):
        edge = set(edge)
        (v1, v2) = tuple(edge)
        if v1 in self.__graph_dict:
            self.__graph_dict[v1].append(v2)
        else:
            self.__graph_dict[v1] = [v2]

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex
            in graph """
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to
            end_vertex in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def vertex_degree(self, vertex):
        adj_vertex = self.__graph_dict[vertex]
        degree = len(adj_vertex) + adj_vertex.count(vertex)
        return  degree

    def delta(self):
        """ the minimum degree of the vertices """
        min = 100000000
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < min:
                min = vertex_degree
        return min

    def Delta(self):
        """ the maximum degree of the vertices """
        max = 0
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > max:
                max = vertex_degree
        return max

    def degree_sequence(self):
        """ calculates the degree sequence """
        seq = []
        for vertex in self.__graph_dict:
            seq.append(self.vertex_degree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)

    @staticmethod
    def is_degree_sequence(sequence):
        """ Method returns True, if the sequence "sequence" is a
            degree sequence, i.e. a non-increasing sequence.
            Otherwise False is returned.
        """
        # check if the sequence sequence is non-increasing:
        return all(x >= y for x, y in zip(sequence, sequence[1:]))

    @staticmethod
    def erdoes_gallai(dsequence):
        """ Checks if the condition of the Erdoes-Gallai inequality
            is fullfilled
            dsequence has to be a valid degree sequence
        """
        if sum(dsequence) % 2:
            # sum of sequence is odd
            return False
        for k in range(1, len(dsequence) + 1):
            left = sum(dsequence[:k])
            right = k * (k - 1) + sum(
                [min(x, k) for x in dsequence[k:]])
            if left > right:
                return False
        return True

    def density(self):
        """ method to calculate the density of a graph """
        g = self.__graph_dict
        V = len(g.keys())
        E = len(self.edges())
        return 2.0 * E / (V * (V - 1))

    def diameter(self):
        """ calculates the diameter of the graph """

        v = self.vertices()
        pairs = [(v[i], v[j]) for i in range(len(v) - 1) for j in
                 range(i + 1, len(v))]
        smallest_paths = []
        for (s, e) in pairs:
            paths = self.find_all_paths(s, e)
            smallest = sorted(paths, key=len)[0]
            smallest_paths.append(smallest)

        smallest_paths.sort(key=len)

        # longest path is at the end of list,
        # i.e. diameter corresponds to the length of this path
        diameter = len(smallest_paths[-1]) - 1
        return diameter


def main():
    graph= { "a" : ["c"],
      "b" : ["c","e","f"],
      "c" : ["a","b","d","e"],
      "d" : ["c"],
      "e" : ["b","c","f"],
      "f" : ["b","e"]
    }

    G = Graph(graph)
    print(G.vertices())
    print(G.edges())
    print(G.isolated_nodes())
    #G.add_vertex("z")
    #G.add_edges({"a","z"})
    print(G)
    print(G.delta())
    print(G.Delta())
    print(G.degree_sequence())
    print(G.diameter())


if __name__ == '__main__':
    main()


