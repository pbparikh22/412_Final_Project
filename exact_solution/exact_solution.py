"""   
    NP Complete Project Exact Solution
    Author: Nicholas Buchan
"""

#Finds all the paths from s to t in the graph
def findAllPaths(graph, s, t):
    visited = [False] * len(graph)
    simples = []

    def pathFinder(graph, s, t, visited, path):
        visited[s] = True
        path.append(s)

        if s == t:
            simples.append(path.copy())
        else:
            for v in graph[s]:
                if visited[v] == False:
                    pathFinder(graph, v, t, visited, path)

        path.pop()
        visited[s] = False

    pathFinder(graph, s, t, visited, [])

    return simples

#Loops through all the paths that were found in the graph
#and calculates their respective length returning the longest ones
def findLongestPath(graph, paths):
    longestPathLength = 0
    longestPath = None
    
    for path in paths:
        currentPath = path
        currentPathLength = 0
        for node in range(len(path)):

            if not node + 1 == len(path): 
                u = path[node]
                v = path[node + 1]
                currentPathLength += graph[u][v]

        if currentPathLength > longestPathLength:
            longestPath = currentPath
            longestPathLength = currentPathLength


    return longestPath, longestPathLength



        
        

def main():
    overveiw = [int(x) for x in input().split()]
    number_of_nodes =  overveiw[0]
    number_of_edges = overveiw[1]
    graph = dict()
    source = 0
    sink = number_of_nodes - 1
    
    for i in range(number_of_nodes):
        graph[i] = dict()

    for index in range(number_of_edges):
        temp = [int(x) for x in input().split()]
        graph[temp[0]][temp[1]] = temp[2]



    solution = findLongestPath(graph, findAllPaths(graph, source, sink))

    print("Longest path: {path}\nLongest Path Length: {length}".format(path = solution[0], length = solution[1]))


if __name__ == "__main__":    

    main()