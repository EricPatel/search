import map
import search

def main():
    # Example graph generation with dimension and probability
    g = map.generateMap(10, 0.3)

    # Path is returned using the graph g
    # The function can be replaced with aStarWithEuclidean, dfs, and aStarWithManhattan
    path = search.aStarWithManhattan(g)

    # Easy way to see the path taken by the algorithm used above
    map.printPath(path, g)

if __name__ == "__main__":
    main()
