import random
from copy import deepcopy
import search

# Spreads the fire on the maze by one time step.
def fireTimeStep(graph, q):
    # Make a deepcopy of the graph, so that fireGraph doesn't reference graph
    fireGraph = deepcopy(graph)
    dim = len(graph)

    # Iterate through the graph and if a cell is open, we need to evaluate
    # whether it should be on fire or not.
    for i in range(dim):
        for j in range(dim):
            if fireGraph[i][j] == 0:

                # Generate the neighbors of cell (i,j)
                neighbors = [(i, j-1), (i,j+1), (i-1, j), (i+1, j)]
                burningNeighbors = 0

                # Count the burning neighbors
                for neighbor in neighbors:
                    x = neighbor[0]
                    y = neighbor[1]
                    if search.checkPoint(x, y, dim) and graph[x][y] == 2:
                        burningNeighbors = burningNeighbors + 1

                # Generate the probability that a cell is on fire using
                # equation in assignment: 1 - (1 - q)^k
                pFire = 1 - ((1 - q)**burningNeighbors)
                randomNum = random.choices(population=[2, 0], weights=[pFire, 1 - pFire], k=1)[0]
                fireGraph[i][j] = randomNum
    return fireGraph

# Generates the shortest path on the map and traverses the graph,
# while spreading the fire every time step. If the fire reaches one of
# cells we are on, than we return failure, otherwise we return the path.
def strategy1(graph, q):
    # Get shortest path on graph
    path = search.aStar(graph, search.euclideanH)

    # Iterate over the path which represents moving over the shortest path
    for x in range(1, len(path)):
        i = path[x][0]
        j = path[x][1]

        # Spread the fire everytime we move on the path
        graph = fireTimeStep(graph, q)

        # Check if the current cell we are on is on fire
        if graph[i][j] == 2:
            return "Failure: No Path"

    return path, graph

# Generates the shortest path on the map every time step and traverses the
# new shortest path while spreading the fire every time step.
# If the fire reaches one of cells we are on, than we return failure,
# otherwise we return the path.
def strategy2(graph, q):
    path = []
    point = (0,0)
    path.append(point)
    dim = len(graph)

    # Recalculate shortest path until the final move is on the goal cell
    while point != (dim-1, dim-1):
        result = search.aStarForStrategy2(point, graph, search.euclideanH)

        # If there is no path, than we immediately return failure
        if result == "Failure: No Path":
            return "Failure: No Path"

        point = result[1]
        i = point[0]
        j = point[1]

        # If the current cell we are on is on fire, than we return failure
        if graph[i][j] == 2:
            return "Failure: No Path"

        graph = fireTimeStep(graph, q)
        path.append(point)

    return path, graph

# Needs to be done
def strategy3(graph, q):
    return None

def distanceToFire(graph, curr):
    dim = len(graph)
    queue = deque()

    # Create a visited array of same dimensions as the graph to ensure that BFS
    # will minimize the fringe size
    visited = [[False for p in range(dim)] for k in range(dim)]


    # Enqueue the starting position and mark it as visited
    queue.append(curr)
    visited[curr[0]][curr[1]] = True

    distance = 0

    # Keep looping while there are elements in the queue
    while len(queue) != 0:
        # Get the first item on the queue
        point = queue.popleft()
        x = point[0]
        y = point[1]

        # Generate a list of all possible neighboring points from the current point (x,y)
        neighbors = [(x, y-1), (x,y+1), (x-1, y), (x+1, y)]
        for neighbor in neighbors:
            i = neighbor[0]
            j = neighbor[1]

            # If we have reached the goal cell, we can return the path associated with
            # that cell.
            if graph[i][j] = 2:
                return count

            # Only append points on the stack if the points are within the bounds
            # of the graph, the point is a 0, and the point has not been visited
            if checkPoint(i, j, dim) and graph[i][j] == 0 and visited[i][j] == False:
                queue.append([i, j])
                visited[i][j] = True
        count += 1
    # If there is no path from source cell to goal cell than return the string below
    return "Failure: No Path"
