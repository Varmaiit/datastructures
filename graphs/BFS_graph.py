# Implementation of linked list in python
# Ref: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/


from collections import defaultdict
        
    
class Graph():

    def __init__(self):
        self.graph = defaultdict(list)
        # print(self.graph, type(self.graph))

    def add_edge(self, u, v):
        self.graph[u].append(v)

    
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * len(self.graph)

        queue = []

        queue.append(s) 
        visited[s] = True
        # print("start", queue, visited, self.graph)

        while queue:

            s = queue.pop(0)
            # print("ss", s, queue)
            print (s, end = " ")

            for i in self.graph[s]: 
                # print("ii", i)
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True


def create_graph():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2) 
    g.add_edge(1, 2) 
    g.add_edge(2, 0) 
    g.add_edge(2, 3) 
    g.add_edge(3, 3)
    return g



if __name__=='__main__': 
    print("Creating Graph......")
    g = create_graph()
    print("Following is the Breadth First Search (starting from vertex 2)")
    g.BFS(2)





    