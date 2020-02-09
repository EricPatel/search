import map
from search import euclideanH, manhattanH, aStar, bfs, bidirectionalBfs, dfs

def main():
    # Example graph generation with dimension and probability
    g = map.generateMap(150, 0.2)
    path = aStar(g, euclideanH)
    bfsPath = bfs(g)

    map.printPath(path, g)
    print(" ")
    map.printPath(bfsPath, g)
    print(" ")
    print(len(path), len(bfsPath))

if __name__ == "__main__":
    main()
