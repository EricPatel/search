import random
import map
from copy import deepcopy
import search
import sys
import heapq
from HeapNode import HeapNode
from collections import deque


# Generates a map given a dimension and a probability that a cell is blocked
# 1 --> Cell is Blocked, 0 --> Cell is Open , 2 --> Cell is on Fire
# Additionally, adds a random starting point for the fire that has a path 
# from source to fire cell.
def generateFireMap(dim, p):
    goal_cell = (dim-1, dim-1)
    source_cell = (0,0)

    # Generate a map with a dim and p for walls 
    graph = map.generateMap(dim, p)

    # If there is no path from the source cell to goal cell
    # discard this map and generate a new one. 
    while search.dfsForFireMap(graph, goal_cell) == False:
        graph = map.generateMap(dim, p)


    # Generate a random coordinate between 0 and dim - 1
    fireX = random.randint(0, dim-1)
    fireY = random.randint(0, dim-1)
    fire_cell = (fireX, fireY)

    # Generate new fire cell starting points if fire starting cell:
    #   - is source cell
    #   - is goal cell
    #   - is a wall (1 in the graph means a wall)
    #   - has no path to source cell
    while fire_cell == source_cell or fire_cell == goal_cell or graph[fireX][fireY] == 1 or search.dfsForFireMap(graph, fire_cell) == False:
        fireX = random.randint(0, dim-1)
        fireY = random.randint(0, dim-1)
        fire_cell = (fireX, fireY)

    graph[fireX][fireY] = 2
    return graph

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
    path = search.aStar(graph, search.manhattanH)[0]

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
        result = search.aStarForStrategy2(point, graph, search.manhattanH)
        
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

def strategy3(graph, q):
    path = []
    point = (0,0)
    path.append(point)
    dim = len(graph)

    # Recalculate shortest path until the final move is on the goal cell
    while point != (dim-1, dim-1):
        result = aStarNew(point,graph, heu)

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
        #map.printMap(g)
        #print("")
        path.append(point)

    return path, graph

def distanceToFire(graph, curr):
    dim = len(graph)
    queue = deque()

    # Create a visited array of same dimensions as the graph to ensure that BFS
    # will minimize the fringe size
    visited = [[False for p in range(dim)] for k in range(dim)]

    # Enqueue the starting position and mark it as visited
    queue.append((curr, 0))
    visited[curr[0]][curr[1]] = True

    # Keep looping while there are elements in the queue
    while len(queue) != 0:
        # Get the first item on the queue
        point = queue.popleft()
        node = point[0]
        x = node[0]
        y = node[1]
        distance = point[1]

        if graph[x][y] == 2:
            return distance
        else:
            # Generate a list of all possible neighboring points from the current point (x,y)
            neighbors = [(x, y-1), (x,y+1), (x-1, y), (x+1, y)]
            for neighbor in neighbors:
                i = neighbor[0]
                j = neighbor[1]

                # Only append points on the stack if the points are within the bounds
                # of the graph, the point is a 0, and the point has not been visited
                if search.checkPoint(i, j, dim) and graph[i][j] != 1 and visited[i][j] == False:
                    queue.append(((i, j), distance + 1))
                    visited[i][j] = True

    # If there is no path from source cell to goal cell than return the string below
    return "Failure: No Path"

def heu(p1, p2, graph):
    distToFire = distanceToFire(graph, p1)
    manDist = search.manhattanH(p1, p2)
    return manDist - distToFire

# Generates a path from the source cell (0,0) to goal cell (dim - 1, dim - 1) using
# A* where heuristicMethod can be euclideanH or manhattanH
def aStarNew(source_cell, graph, heuristicMethod):
    dim = len(graph)    
    goal_cell = (dim-1, dim-1)
    
    # Dictionary where the key is the cell and the value is the 
    # cell that was previous. This is used to generate the actual path. 
    prevMap = {}

    # Create a visited array of same dimensions as the graph which will make sure
    # that A* considers only cells that have not been visited which will reduce 
    # the maximum fringe size and prevent cycles. Every position is initialized
    # to the maximum integer to make sure the correct path is found. 
    visited = [[sys.maxsize for p in range(dim)] for k in range(dim)]

    # Create a min-heap/priority queue to use for A*
    heap = []
    heapq.heapify(heap)

    # Start by appending the estimated distance from the source cell to the goal cell,
    # the source cell, the previous cell, and the distance from the source.
    # This heap will automatically use the first value in the tuple to sort the items
    # because of the __lt__ method in our HeapNode class.
    first_node = HeapNode(heuristicMethod(source_cell, goal_cell, graph), source_cell, None, 0)
    
    prevMap[source_cell] = None
    heapq.heappush(heap, first_node)
    visited[source_cell[0]][source_cell[1]] = heuristicMethod(source_cell, goal_cell, graph)

    while len(heap) != 0:
        node = heapq.heappop(heap)
        point = node.cell
        x = point[0]
        y = point[1]

        # If we have reached the goal cell, we can return the path associated with
        # that cell.
        if x == dim - 1 and y == dim - 1:
            return search.getPath(prevMap, goal_cell)
        else:
            # Generate a list of all possible neighboring points from the current point (x,y)
            points = [(x, y-1), (x,y+1), (x-1, y), (x+1, y)]
            for (i,j) in points:
                if search.checkPoint(i, j, dim):

                    # The distance from the source to the current point (i,j)
                    neighborToSource = node.distFromSource + 1

                    # The estimated distance from the neighbor to the goal cell
                    neighborPointHeuristic = heuristicMethod((i,j), goal_cell, graph)

                    totalDistanceToGoal = neighborToSource + neighborPointHeuristic

                    # Only append points on the heap if the points are within the bounds
                    # of the graph, the point is a 0, and the point has a smaller total distance
                    # than visited[i][j].
                    if graph[i][j] == 0 and visited[i][j] > totalDistanceToGoal:
                        visited[i][j] = totalDistanceToGoal
                        prevMap[(i,j)] = point
                        neighbor = HeapNode(totalDistanceToGoal, (i,j), point, neighborToSource)
                        heapq.heappush(heap, neighbor)
                    
    # If there is no path from source cell to goal cell than return the string below
    return "Failure: No Path"

