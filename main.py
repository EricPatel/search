import map
import search

def main():
    # Example graph generation with dimension and probability
    g = map.generateMap(10, 0.3)
    # Path is returned using the graph g
    # The function can be replaced with aStarWithEuclidean, dfs, and aStarWithManhattan
    print("Manhattan")
    path = search.aStarWithManhattan(g)
    map.printMap(g)
    print("")
    map.printPath(path, g)
    print("")
    bpath = search.dfs(g)
    map.printPath(bpath, g)
    print(len(path), len(bpath))
    #print("Euclidean")
    #path2 = search.aStarWithEuclidean(g)
    #map.printPath(path2, g)
    #print("")
    #dfsPath = search.dfs(g)
    #bfsPath = search.bfs(g)
    #biBFSPath = search.bidirectionalBfs(g)
    # Easy way to see the path taken by the algorithm used above
    """map.printPath(dfsPath, g)
    print("")
    map.printPath(bfsPath, g)
    print("")
    map.printPath(biBFSPath, g)"""

if __name__ == "__main__":
    main()
