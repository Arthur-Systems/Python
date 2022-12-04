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

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def depth_first_search(self):
        for v in self.vertList.values():
            v.color = 'white'
        path = []  # not a part of DFS, used to check the order of vertices traversed by DFS
        for v in self.vertList.values():
            if v.color == 'white':
                self.DFS(v.id, path)
        return path

    def DFS(self, vid, path):
        v = self.vertList[vid]
        v.color = 'gray'
        path.append(v.id)
        for u in v.connectedTo.keys():
            if u.color == 'white':
                self.DFS(u.id, path)
        v.color = 'black'
        return path


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.vertList

    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    for v in g:
        print(v)
    path = g.depth_first_search()
    print('DFS traversal: ', path)
