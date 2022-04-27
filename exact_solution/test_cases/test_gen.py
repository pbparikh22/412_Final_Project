"""   
    Test Generator
    Author: Nicholas Buchan
"""
import random



        
        

def main():
    #Takes in #of Nodes #of Edges
    number_of_nodes = 30
    graph = dict()

    prev = 0
    for i in range(number_of_nodes):
        graph[i] = dict()
        if not i == 0:
            graph[prev][i] = random.randint(1, 100)
            if not i == number_of_nodes - 1:
                graph[prev][i + 1] = random.randint(1, 100)
        prev = i
        
            

    number_of_edges = -1
    output = ""
    for i in graph:
        for v in graph[i]:
            number_of_edges += 1
            output += ("{u} {v} {w}\n".format(u = i, v = v, w = graph[i][v]))

    print("{n} {e}".format(n = number_of_nodes, e = number_of_edges))
    print(output)




if __name__ == "__main__":    

    main()