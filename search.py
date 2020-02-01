import heapq
import math

# Helper function to check if a certain point is between 0 and the graphs dimensions
def checkPoint(x, y, dim):
    if x >= 0 and x < dim and y >= 0 and y < dim:
        return True
    return False

# Generates a path from the source cell (0,0) to goal cell (dim - 1, dim - 1) using 
# Depth-First Search. 
def dfs(graph):
    # Create a stack to use for DFS
    stack = []
    dim = len(graph)

    # Create a visited array of same dimensions as the graph to ensure that DFS
    # does not run forever.
    visited = [[False for p in range(dim)] for k in range(dim)]

    # Start by appending the source cell with the current path
    # The first element in the list is the x-value, second value is the 
    # y-value, and third value is a list of tuples which represents the
    # path DFS took to that cell.
    stack.append([0,0,[(0,0)]])

    while len(stack) != 0:
        point = stack.pop()
        x = point[0]
        y = point[1]
        path = point[2].copy()
        visited[x][y] = True
        
        # If we have reached the goal cell, we can return the path associated with
        # that cell. 
        if x == dim - 1 and y == dim - 1:
            return path
        else:
            # Generate a list of all possible neighboring points from the current point (x,y)
            points = [(x, y-1), (x,y+1), (x-1, y), (x+1, y)]
            for (i,j) in points:
                path = point[2].copy()
                # Only append points on the stack if the points are within the bounds
                # of the graph, the point is a 0, and the point has not been visited
                if checkPoint(i, j, dim) and graph[i][j] == 0 and visited[i][j] == False:
                    path.append((i,j))
                    stack.append([i, j, path])

    # If there is no path from source cell to goal cell than return the string below
    return "Failure: No Path"

# Generates a path from the source cell (0,0) to goal cell (dim - 1, dim - 1) using
# A* where the heuristic is the euclidean distance
def aStarWithEuclidean(graph):
    dim = len(graph)
    source_cell = (0,0)
    goal_cell = (dim-1, dim-1)

    # Create a visited array of same dimensions as the graph which will make sure
    # that A* considers only cells that have not been visited which will reduce 
    # the maximum fringe size.
    visited = [[False for p in range(dim)] for k in range(dim)]

    # Create a min-heap/priority queue to use for A*
    heap = []
    heapq.heapify(heap)

    # Start by appending the euclidean distance from the source cell to the goal cell
    # with the source cell and the current path.
    # This heap will automatically use the first value in the tuple to sort the items.
    heapq.heappush(heap, (euclideanH(source_cell, goal_cell), source_cell, [source_cell]))

    while len(heap) != 0:
        item = heapq.heappop(heap)
        point = item[1]
        x = point[0]
        y = point[1]
        path = item[2].copy()
        visited[x][y] = True

        # If we have reached the goal cell, we can return the path associated with
        # that cell.
        if x == dim - 1 and y == dim - 1:
            return path
        else:
            # Generate a list of all possible neighboring points from the current point (x,y)
            points = [(x, y-1), (x,y+1), (x-1, y), (x+1, y)]
            for (i,j) in points:
                path = item[2].copy()
                # Only append points on the stack if the points are within the bounds
                # of the graph, the point is a 0, and the point has not been visited
                if checkPoint(i, j, dim) and graph[i][j] == 0 and visited[i][j] == False:
                    # Distance between the source cell and (i,j) will be the length of the path
                    # before adding (i,j) to the path
                    realDistance = len(path)

                    # Add the point (i,j) to the current path
                    path.append((i,j))

                    # When adding the point (i,j) to the heap, we must use the actual distance between
                    # source cell and (i,j) + the euclidean distance between (i,j) to the 
                    # goal cell.
                    heapq.heappush(heap, (realDistance + euclideanH((i,j), goal_cell), (i,j), path))
                    
    # If there is no path from source cell to goal cell than return the string below
    return "Failure: No Path"

# Generates a path from the source cell (0,0) to goal cell (dim - 1, dim - 1) using
# A* where the heuristic is the manhattan distance
def aStarWithManhattan(graph):
    dim = len(graph)
    source_cell = (0,0)
    goal_cell = (dim-1, dim-1)

    # Create a visited array of same dimensions as the graph which will make sure
    # that A* considers only cells that have not been visited which will reduce 
    # the maximum fringe size.
    visited = [[False for p in range(dim)] for k in range(dim)]

    # Create a min-heap/priority queue to use for A*
    heap = []
    heapq.heapify(heap)

    # Start by appending the manhattan distance from the source cell to the goal cell
    # with the source cell and the current path.
    # This heap will automatically use the first value in the tuple to sort the items.
    heapq.heappush(heap, (manhattanH(source_cell, goal_cell), source_cell, [source_cell]))

    while len(heap) != 0:
        item = heapq.heappop(heap)
        point = item[1]
        x = point[0]
        y = point[1]
        path = item[2].copy()
        visited[x][y] = True

        # If we have reached the goal cell, we can return the path associated with
        # that cell.
        if x == dim - 1 and y == dim - 1:
            return path
        else:
            # Generate a list of all possible neighboring points from the current point (x,y)
            points = [(x, y-1), (x,y+1), (x-1, y), (x+1, y)]
            for (i,j) in points:
                path = item[2].copy()
                if checkPoint(i, j, dim) and graph[i][j] == 0 and visited[i][j] == False:
                    # Distance between the source cell and (i,j) will be the length of the path
                    # before adding (i,j) to the path
                    realDistance = len(path)

                    # Add the point (i,j) to the current path
                    path.append((i,j))

                    # When adding the point (i,j) to the heap, we must use the actual distance between
                    # source cell and (i,j) + the manhattan distance between (i,j) to the 
                    # goal cell.
                    heapq.heappush(heap, (realDistance + manhattanH((i,j), goal_cell), (i,j), path))
                    
    # If there is no path from source cell to goal cell than return the string below
    return "Failure: No Path"

# Generates the euclidean distance between two points.
# Will be used for the aStarWithEuclidean function
def euclideanH(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# Generates the manhattan distance between two points.
# Will be used for the aStarWithManhattan function
def manhattanH(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

