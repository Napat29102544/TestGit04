def run_01():
    class Graph:
        def __init__(self):
            self.vertices = {}

        def add_vertex(self, vertex):
            if vertex not in self.vertices:
                self.vertices[vertex] = {}

        def add_edge(self, vertex1, vertex2, weight):
            if vertex1 in self.vertices and vertex2 in self.vertices:
                self.vertices[vertex1][vertex2] = weight
                self.vertices[vertex2][vertex1] = weight  # For an undirected graph

        def display(self):
            for vertex, neighbors in self.vertices.items():
                for neighbor, weight in neighbors.items():
                    print(f"{vertex},{neighbor},{weight}")

    def run01():
        # Create a graph instance
        the_graph = Graph()
        # Vertex
        the_graph.add_vertex('A')
        the_graph.add_vertex('B')
        the_graph.add_vertex('C')
        the_graph.add_vertex('D')
        # Edges
        the_graph.add_edge('A', 'B', 3)
        the_graph.add_edge('B', 'C', 5)
        the_graph.add_edge('C', 'D', 7)
        the_graph.add_edge('D', 'A', 9)

        the_graph.display()

    print(run01())


def run_02():
    n = 3                                                                               # there are three nodes in example graph (graph is 1-based)
    dist = [[0, 5, 10, 25], [10, 0, 5, 20], [15, 20, 0, 10], [30, 15, 25, 0]]           # Distance between city
    memo = [[-1] * (1 << (n + 1)) for _ in range(n + 1)]                                # memoization for top down recursion

    def fun(i, city):                                                                   # sub-problem
        if city == ((1 << i) | 3):
            return dist[1][i]                                                           # it implies we have visited all other nodes already

        if memo[i][city] != -1:                                                         # memoization
            return memo[i][city]
        result = 99                                                                     # result of this sub-problem

        for j in range(1, n + 1):                                                       # we have to travel all nodes j in mask and end the path at last node
            if (city & (1 << j)) != 0 and j != i and j != 1:                            # travelling all nodes in mask except i and then travel back from node j to node i taking
                result = min(result, fun(j, city & (~(1 << i))) + dist[j][i])           # the shortest path take the minimum of all possible j nodes
        memo[i][city] = result                                                          # storing the minimum value
        return result

    ans = 99
    for i in range(1, n + 1):                                                           # try to go from node 1 visiting all nodes in between to i
        ans = min(ans, fun(i, (1 << (n + 1)) - 1) + dist[i][1])                         # return from i taking the shortest route to 1

    print("The cost of most efficient tour = " + str(ans))
