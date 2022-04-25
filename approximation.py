"""
    names: Seth Walter

    approximation solution for longest path np-complete
"""
def main():
    # read input into an adjacency list

    # start our longest_path_approx from the source node
    # if finding a general longest path, start algorithm from each node

    # print path found and weight of path
    pass

def longest_path_approx():
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