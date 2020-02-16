import map
from search import euclideanH, manhattanH, aStar, bfs, bidirectionalBfs, dfs
import fire

def main():
    # Example graph generation with dimension and probability
    g = map.generateMap(150, 0.2)
    path = aStar(g, manhattanH)
    bfsPath = bfs(g)

    map.printPath(path, g)
    print(" ")
    map.printPath(bfsPath, g)
    print(" ")
    print(len(path), len(bfsPath))

    # Example for visualizing path for graph g
    map.visualize(path, g)
    map.visualize(bfsPath, g)

    # Example fire graph generation with dimension and probability
    fireG = map.generateFireMap(100, 0.3)

    # Strategies with Flammability rate q
    q = 0.1
    result1 = fire.strategy1(fireG, q)
    result2 = fire.strategy2(fireG, q)

    map.printPath(result1[0], result1[1])
    print("")
    map.printPath(result2[0], result2[1])

    # Example for visualizing path for fire graph g where the first element 
    # in the result tuple is the path and second element is the final graph. 
    map.visualizeFireMap(result1[0], result1[1])
    map.visualizeFireMap(result2[0], result2[1])


if __name__ == "__main__":
    main()
