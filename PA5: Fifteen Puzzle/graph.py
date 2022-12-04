# author: Arthur Wei
# date: November 14, 2022
# file: Graph.py a python file that creates a graph implementation of fifteen puzzle
# input: User inputted commands
# output: Graph of fifteen puzzle

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):  # add a vertex to the graph
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):  # get a vertex from the graph
        for v in self.vertList.values():
            if v.id == n:
                return v

    def __contains__(self, n):
        return n in self.vertList.values()

    def addEdge(self, f, t, weight=0):  # add an edge to the graph
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()  # return the vertices of the graph

    def __iter__(self):
        return iter(self.vertList.values())  # return the graph

    def breadth_first_search(self, s):
        visited = [s]  # list of visited vertices
        queue = [s]
        while queue:  # while the queue is not empty
            s = queue.pop(0)
            for v in self.vertList.values():
                if v.id == s:  # if the vertex is the one we are looking for
                    for w in v.getConnections():
                        if w.id not in visited:
                            # add the vertex to the list of visited vertices
                            visited.append(w.id)
                            queue.append(w.id)  # add the vertex to the queue
        return visited  # return the list of visited vertices

    def depth_first_search(self):
        visited = []  # list of visited vertices
        self.DFS(0, visited)  # call the recursive function
        return visited  # return the list of visited vertices

    def DFS(self, vid, path):
        path.append(vid)
        # for each neighbor of the vertex
        for neighbor in self.vertList[vid].getConnections():
            if neighbor.id not in path:
                self.DFS(neighbor.id, path)  # call the function recursively


if __name__ == '__main__':

    g = Graph()
    for i in range(6):
        g.addVertex(i)

    g.addEdge(0, 1)
    g.addEdge(0, 5)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 0)
    g.addEdge(5, 4)
    g.addEdge(5, 2)

    for v in g:
        print(v)

    assert (g.getVertex(0) in g) == True
    assert (g.getVertex(6) in g) == False

    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'

    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'

    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]

    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]
