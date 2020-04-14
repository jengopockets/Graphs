"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} #Ajacency List

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            #add the edge
            self.vertices[v1].add(v2)
        else:
            print("Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # visited = [False] * (len(self.vertices))
        # print(visited)
        #Pull up queue
        queue = Queue()
        # Enqueue start point
        queue.enqueue([starting_vertex])
        visited = set()
        # while queue is not empty
        while queue.size() > 0:
            #dequeue the first vertex
            path = queue.dequeue()
            # if not visited
            if path[-1] not in visited:
                #Do the thing
                print(path[-1])
                #mark visited
                visited.add(path[-1])
                #enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)    
            

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # set up stack
        stack = Stack()
        # push first verticies to stack
        stack.push([starting_vertex])
        visited = set()
        # While stack isn't empty
        while stack.size() > 0:
            #pop of stack
            path = stack.pop()
            if path[-1] not in visited:
                #do thing
                print(path[-1])
                #mark visited
                visited.add(path[-1])
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)            


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        #Recusion function inside to keep for infinet loop
        def dft_recursion(vertex):
            # Checks if vertex has been visited    
            if vertex in visited:
                return
            #Adds vertex to visited and prints
            visited.add(vertex)
            print(vertex)
            #Recursion occures to find next vertex
            for i in self.vertices[vertex]:
                dft_recursion(i)
        
        dft_recursion(starting_vertex)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        # Enqueue starting vertex
        queue.enqueue([starting_vertex])
        #Set to track visited
        visited = set()
        #While queue not empty
        while queue.size() > 0:
            #dequeue first Path
            path = queue.dequeue()
            # get the last vertex from path
            last_vertex = path[-1]
            # Check if it has been visited
            if last_vertex not in visited:
                #Check if it is the destination
                if last_vertex == destination_vertex:
                    return path
                #Add to visited
                visited.add(last_vertex)
                #Add neigbors to back of queue
                for i in self.vertices[last_vertex]:
                    #Clone Path
                    new_path = [*path]
                    # Add neigbor to back of queue
                    new_path.append(i)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #Set up stack
        stack = Stack()
        #Push starting vertex to stack
        stack.push([starting_vertex])
        visited = set()

        while stack.size() > 0:
            path = stack.pop()
            last_vertex = path[-1]
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return path
                visited.add(last_vertex)
                for i in self.vertices[last_vertex]:
                    new_path = [*path]
                    new_path.append(i)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        path = []

        def dfs_recusion(start_vert, dest_vert, path):
            if start_vert in visited:
                return path
            elif start_vert == dest_vert:
                path.append(start_vert)
                return path
            visited.add(start_vert)
            for i in self.vertices[start_vert]:
                if dest_vert in dfs_recusion(i, dest_vert, path):
                    path.append(start_vert)
                    return path
            return path
        solu = dfs_recusion(starting_vertex, destination_vertex, path)
        return solu[::-1]

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
