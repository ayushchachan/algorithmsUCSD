def read_directed_graph():
    numVertices, numEdges = list(map(int, input().split()))

    g = dict()

    for u in range(1, numVertices + 1):
        g[u] = set()
    
    for i in range(numEdges):
        u, v = list(map(int, input().split()))
        
        g[u].add(v)
    return g

def read_undirected_graph():
    numVertices, numEdges = list(map(int, input().split()))

    g = dict()

    for u in range(1, numVertices + 1):
        g[u] = set()

    for i in range(numEdges):
        u, v = list(map(int, input().split()))
        
        g[u].add(v)
        g[v].add(u)
    return g

def read_directed_graph_file(filename):
    f = open(filename)
    numVertices, numEdges = list(map(int, f.readline().split()))

    g = dict()

    for u in range(1, numVertices + 1):
        g[u] = set()
    
    for i in range(numEdges):
        u, v = list(map(int, f.readline().split()))
        
        g[u].add(v)
    return g
