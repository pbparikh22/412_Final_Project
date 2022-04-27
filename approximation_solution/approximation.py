"""
    names: Seth Walter

    approximation solution for longest path np-complete

    this is a greedy algorithm that favors longest edge 
    weights (edges with greatest weight)
"""


def main():
    num_vertices, num_edges = [int(i) for i in input().split()]
    graph_input = [[int(i) for i in [input()][0].split()] for _ in range(num_edges)]

    # write input into an adjacency list
    graph = {}
    for edge in graph_input:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []
        graph[edge[0]].append((edge[1],edge[2]))
    

    for u in graph:
        graph[u].sort(reverse=True, key=lambda v:v[1])
    
    # change these values later to be read in from input
    s = 0
    t = num_vertices - 1 # this isn't actually a sink node, just where our graph ends

    # start our longest_path_approx from the source node
    # if finding a general longest path, start algorithm from each node
    path = longest_path_approx(graph, s, t)

    max_path = []
    max_weight = 0
    v = s
    max_path.append(str(v))
    while v in path:
        max_weight += path[v][1]
        v = path[v][0]
        max_path.append(str(v))
    max_path = [int(i) for i in max_path]
    print("Longest Path:", max_path)
    print("Longest Path Length:", max_weight)
    
"""def longest_path_approx_DFS(graph, v, visited, path, t):
    visited[v] = 0
    if t in path:
        return True
    for k in path:
        if t == path[k][0]:
            return True
    for u in graph[v]:
        #if path != None: dont think I need this anymore
        path[v] = (u[0], u[1])
        isTrue = longest_path_approx_DFS(graph, u[0], visited, path, t)
        if isTrue:
            return True
    return False"""

def longest_path_approx(graph, s, t):
    # Need to make this dfs, its using bfs right now
    # NOTE the ending node is also broken, needs to be fixed to stop if it finds the end node
    visited = {}
    visited[s] = 0
    path = {}
    def longest_path_approx_DFS(graph, v, visited, path, t):
        if t in path:
            return True
        for k in path:
            if t == path[k][0]:
                return True
        for u in graph[v]:
            if u not in visited:
                visited[u] = 0
            #if path != None: dont think I need this anymore
                path[v] = (u[0], u[1])
                isTrue = longest_path_approx_DFS(graph, u[0], visited, path, t)
                if isTrue:
                    return True
        return False

    longest_path_approx_DFS(graph, s, visited, path, t)
    return path

if __name__ == "__main__":
    main()