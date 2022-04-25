"""   
    NP Complete Project Exact Solution
    Author: Nicholas Buchan
"""


        
        

def main():
    overveiw = [int(x) for x in input().split()]
    number_of_nodes =  overveiw[0]
    number_of_edges = overveiw[1]
    graph = dict()
    for i in range(number_of_nodes):
        graph[i] = dict()

    for index in range(number_of_edges):
        temp = [int(x) for x in input().split()]
        graph[temp[0]][temp[1]] = temp[2]

    print(graph)


if __name__ == "__main__":    

    main()