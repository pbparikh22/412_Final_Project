"""
    names: Seth Walter

    approximation solution for longest path np-complete
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
    
    # change these values later to be read in from input
    s = 0
    t = 5

    # start our longest_path_approx from the source node
    # if finding a general longest path, start algorithm from each node
    path, max_weight = longest_path_approx(graph, s, t)

    max_path = []
    v = s
    max_path.append(str(v))
    while v != t:
        v = path[v]
        max_path.append(str(v))
    print(" => ".join(max_path))
    print("Max weight of this path is", max_weight)
    

def longest_path_approx(graph, s, t):
    # Need to make this dfs, its using bfs right now
    # NOTE the ending node is also broken, needs to be fixed to stop if it finds the end node
    max_weight = 0
    visited = {}
    path = {}
    stack = []
    stack.append(s)
    while len(stack) != 0:
        max_edge = (-1, -1)
        u = stack.pop()
        if u == t:
            break
        for v in graph[u]:
            if v[0] not in visited:
                visited[u] = v[0]
                if v[1] > max_edge[1]:
                    max_edge = (v[0], v[1])
        if max_edge[0] != -1:
            max_weight += max_edge[1]
            path[u] = max_edge[0]
            stack.append(max_edge[0])
    return path, max_weight

    # we want to use dfs here to search for paths

    # general idea is to find the heaviest edge weight, pick it and then
    # continue to pick heaviest edge weights from there. Greedy approach

    # other ideas include starting from second largest edge weight, third largest
    # etc.

    # we can also make this an anytime algorithm by allowing the greedy approach
    # to keep searching and as time goes on hope it finds a better approximation
    # NOTE probably wont do this just an idea
    pass

if __name__ == "__main__":
    main()