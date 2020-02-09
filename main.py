import map
import search

def main():
    # Example graph generation with dimension and probability
    g = map.generateMap(20, 0.3)
    #g = [[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[0,1,0,1,1],[0,1,0,0,0]]
    # Path is returned using the graph g
    # The function can be replaced with aStarWithEuclidean, dfs, and aStarWithManhattan
    path = search.aStar(g, search.manhattanH)
    #path2 = search.aStar(g, search.euclideanH)
    dfsPath = search.dfs(g)
    bfsPath = search.bfs(g)
    # Easy way to see the path taken by the algorithm used above
    print(len(path))
    map.printPath(path, g)
    print("")
    #print(len(path2))
    #map.printPath(path2, g)
    print("")
    print(len(dfsPath))
    map.printPath(dfsPath, g)
    print("")
    print(len(bfsPath))
    map.printPath(bfsPath, g)

if __name__ == "__main__":
    main()
