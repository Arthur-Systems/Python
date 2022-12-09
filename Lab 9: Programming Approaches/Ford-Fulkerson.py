class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for i, val in enumerate(self.graph[u]):  # get adj list
                if visited[i] == False and val > 0:  # get neighbors
                    queue.append(i)
                    visited[i] = True
                    parent[i] = u
        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        for i in range(len(parent)):
            print(i, parent[i], end='; ')
        print()
        return max_flow


if __name__ == '__main__':
    # problem 1 an example of a network flow graph
    adj = [[0, 8, 0, 0, 3, 0],
           [0, 0, 9, 0, 0, 0],
           [0, 0, 0, 2, 7, 2],
           [0, 0, 0, 0, 0, 5],
           [0, 0, 7, 4, 0, 0],
           [0, 0, 0, 0, 0, 0]]
    g = Graph(adj)
    source, sink = 0, 5
    print("Max Flow: %d " % g.ford_fulkerson(source, sink))

    # problem 2 an example of a network flow with a bipartite graph
    adj = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    g = Graph(adj)
    source, sink = 0, 9
    print("Max Flow: %d " % g.ford_fulkerson(source, sink))
