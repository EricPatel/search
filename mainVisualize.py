import map
import searchV
import sys 

def main():
    g = map.generateMap(150, 0.3)
    path = searchV.aStar(g, searchV.manhattanH)
    while path == "Failure: No Path":
        g = map.generateMap(150, 0.3)
        path = searchV.aStar(g, searchV.manhattanH)

    m_visited = path[1]
    path = path[0]
    path2, e_visited, e_time = searchV.aStar(g, searchV.euclideanH)
    biBFSpath, bi_visited, bi_time = searchV.bidirectionalBfs(g)

    # A* with Manhattan
    map.visualizeWithNodesVisited(path, g, m_visited, sys.maxsize)

    # A* with Euclidean
    map.visualizeWithNodesVisited(path2, g, e_visited, sys.maxsize)

    # Bidirectional Breadth First Search
    map.visualizeWithNodesVisited(biBFSpath, g, bi_visited, 0)


if __name__ == "__main__":
    main()