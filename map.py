import random

# Generates a map given a dimension and a probability that a cell is blocked
# 1 --> Cell is Blocked, 0 --> Cell is Open
def generateMap(dim, p):
    graph = []

    # These two loops are used initialize the graph with the correct values
    for i in range(dim):
        row = []
        for j in range(dim):
            # Random.choices function is an inbuilt python function that takes 
            # a list of choices and respective weights that returns a choice.
            # In this case, our two choices are 1 for a cell being blocked and 
            # 0 for a cell being clear/open. 
            randomNum = random.choices(population=[1, 0], weights=[p, 1 - p], k=1)[0]
            row.append(randomNum)
        graph.append(row)

    # Ensures that the source cell (0,0) is open and the goal cell (dim - 1, dim - 1)
    # is open, as they may have been initialized to 1 in the previous for loops
    graph[0][0] = 0
    graph[dim-1][dim-1] = 0
    return graph

# Helper Function used to print graphs in a pretty way
def printMap(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j], end=" ")
        print("")

# Helper function that takes in a list of points as a path and a graph.
# Prints out the graph with the points taken shown as "-"
def printPath(path, graph):
    if type(path) == str:
        print("No Valid Path")
        return
    p = set(path)
    for i in range(len(graph)):
        for j in range(len(graph)):
            if (i,j) in p:
                print("-", end=" ")
            else:
                print(graph[i][j], end=" ")
        print("")
