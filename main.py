import map
from search import euclideanH, manhattanH, aStar, bfs, bidirectionalBfs, dfs
import fire

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

    

    # Example fire graph generation with dimension and probability
    fireG = fire.generateFireMap(150, 0.3)

    # Strategies with Flammability rate q
    q = 0.1
    result1 = fire.strategy1(fireG, q)
    result2 = fire.strategy2(fireG, q)

    map.printPath(result1[0], result1[1])
    print("")
    map.printPath(result2[0], result2[1])

if __name__ == "__main__":
    main()
