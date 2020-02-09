import map
import search

def main():
    # Example graph generation with dimension and probability
    g = map.generateMap(20, 0.3)
    #g = [[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[0,1,0,1,1],[0,1,0,0,0]]
    # Path is returned using the graph g
    # The function can be replaced with aStarWithEuclidean, dfs, and aStarWithManhattan
    print("A* manhattan")
    path = search.aStar(g, search.manhattanH)
    print(len(path))
    map.printPath(path, g)
    print("")

    print("A* euclidean")
    path2 = search.aStar(g, search.euclideanH)
    print(len(path2))
    map.printPath(path2, g)
    print("")

    print("dfs")
    dfsPath = search.dfs(g)
    print(len(dfsPath))
    map.printPath(dfsPath, g)
    print("")

    print("bfs")
    bfsPath = search.bfs(g)
    print(len(bfsPath))
    map.printPath(bfsPath, g)
    print("")

    print("bd-bfs")
    bdBFSPath = search.bidirectionalBfs(g)
    print(len(bdBFSPath))
    map.printPath(bdBFSPath, g)
    print("")
    
    # Easy way to see the path taken by the algorithm used above
    
    

if __name__ == "__main__":
    main()
