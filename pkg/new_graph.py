# class Graph:
#     def __init__(self, num_vertices):
#         self.graph = list()
#         for _ in range(num_vertices):
#             temp = list()
#             for _ in range(num_vertices):
#                 temp.append(False)
#             self.graph.append(temp)

#     def add_edge(self, u, v):
#         self.graph[u][v] = True
#         self.graph[v][u] = True

#     # don't touch below this line

#     def edge_exists(self, u, v):
#         if u < 0 or u >= len(self.graph):
#             return False
#         if len(self.graph) == 0:
#             return False
#         row1 = self.graph[0]
#         if v < 0 or v >= len(row1):
#             return False
#         return self.graph[u][v]
    

# class Graph:
#     def __init__(self):
#         self.graph = dict()

#     def add_edge(self, u, v):
#         if u  not in self.graph:
#             self.graph[u] = set()
#         if v  not in self.graph:
#             self.graph[v] = set()
#         self.graph[u].add(v)
#         self.graph[v].add(u)

#     # don't touch below this line

#     def edge_exists(self, u, v):
#         if u in self.graph and v in self.graph:
#             return (v in self.graph[u]) and (u in self.graph[v])
#         return False


# class Graph:
#     def adjacent_nodes(self, node):
#         return self.graph[node]

#     # don't touch below this line

#     def __init__(self):
#         self.graph = {}

#     def add_edge(self, u, v):
#         if u in self.graph:
#             self.graph[u].add(v)
#         else:
#             self.graph[u] = {v}
#         if v in self.graph:
#             self.graph[v].add(u)
#         else:
#             self.graph[v] = {u}


class Graph:
    def unconnected_vertices(self):
        result_list = list()
        for k in self.graph:
            if  len(self.graph[k]) == 0:
                result_list.append(k)
        return result_list

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()



