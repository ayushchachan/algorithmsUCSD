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


def dfs_visit(Adj, u, visit, isActive):
    #non recursive implementation of dfs
    isActive[u] = True
    visit[u] = True

    for v in Adj[u]:
        if v not in visit:
            isThereCycle = dfs_visit(Adj, v, visit, isActive)
            if isThereCycle:
                return True
        elif isActive[v]:
            return True
    isActive[u] = False
    return False
    


def containsCycle(Adj):
    numVertices = len(Adj)
    visit = {}
    isActive = {}
    for u in range(1, numVertices + 1):
        isActive[u] = False

    for u in range(1, numVertices + 1):
        ## dfs_visit(u)
        
        isThereCycle = dfs_visit(Adj, u, visit, isActive)
        if isThereCycle:
            return 1
    return 0


# Adj = read_directed_graph_file("graph1.txt")
Adj = read_directed_graph()
print(containsCycle(Adj))