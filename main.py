import map
import search

def main():
    # Example graph generation with dimension and probability

    for i in range(10, 45, 5):
        avg_visited_euclidean = 0
        avg_visited_manhattan = 0
        avg_visited_dfs = 0
        avg_visited_bfs = 0
        avg_visited_biBFS = 0
        avg_time_euclidean = 0
        avg_time_manhattan = 0
        avg_time_dfs = 0
        avg_time_bfs = 0
        avg_time_biBFS = 0
        for j in range(10):
            g = map.generateMap(150, i/100)
            path = search.aStar(g, search.manhattanH)
            while len(path) == 16:
                g = map.generateMap(150, i/100)
                path = search.aStar(g, search.manhattanH)
            m_visited = path[1]
            m_time = path[2]
            path = path[0]

            path2, e_visited, e_time = search.aStar(g, search.euclideanH)
            dfsPath, d_visited, d_time = search.dfs(g)
            bfsPath, b_visited, b_time = search.bfs(g)
            biBFSpath, bi_visited, bi_time = search.bidirectionalBfs(g)

            avg_time_euclidean = avg_time_euclidean + e_time
            avg_time_manhattan = avg_time_manhattan + m_time
            avg_visited_euclidean = avg_visited_euclidean + e_visited
            avg_visited_manhattan = avg_visited_manhattan + m_visited
            avg_time_dfs = avg_time_dfs + d_time
            avg_time_bfs = avg_time_bfs + b_time
            avg_time_biBFS = avg_time_biBFS + bi_time
            avg_visited_dfs = avg_visited_dfs + d_visited
            avg_visited_bfs = avg_visited_bfs + b_visited
            avg_visited_biBFS = avg_visited_biBFS + bi_visited

        print("A* Euclidean Numbers where P = " + str(i/100))
        print("Avg Visited Nodes: " + str(avg_visited_euclidean/10))
        print("Avg Time: " + str(avg_time_euclidean/10))

        print("")

        print("A* Manhattan Numbers where P = " + str(i/100))
        print("Avg Visited Nodes: " + str(avg_visited_manhattan/10))
        print("Avg Time: " + str(avg_time_manhattan/10))

        print("")

        print("DFS Numbers where P = " + str(i/100))
        print("Avg Visited Nodes: " + str(avg_visited_dfs/10))
        print("Avg Time: " + str(avg_time_dfs/10))

        print("")

        print("BFS Numbers where P = " + str(i/100))
        print("Avg Visited Nodes: " + str(avg_visited_bfs/10))
        print("Avg Time: " + str(avg_time_bfs/10))

        print("")

        print("BiDirectional BFS Numbers where P = " + str(i/100))
        print("Avg Visited Nodes: " + str(avg_visited_biBFS/10))
        print("Avg Time: " + str(avg_time_biBFS/10))

        print("")

            
    #g = [[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[0,1,0,1,1],[0,1,0,0,0]]
    # Path is returned using the graph g
    # The function can be replaced with aStarWithEuclidean, dfs, and aStarWithManhattan
    
    
    """print("A* manhattan")
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
    print("")"""
    
    # Easy way to see the path taken by the algorithm used above
    
    

if __name__ == "__main__":
    main()
