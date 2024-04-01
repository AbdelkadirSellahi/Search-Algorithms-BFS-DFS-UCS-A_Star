# Definition of the graph as a dictionary, where each node is a key, and its values are the nodes it's directly connected to.
graphe = {
    'A': ['B', 'D', 'H'],
    'B': ['F'],
    'C': ['D'],
    'D': ['E', 'G'],
    'E': ['A', 'C', 'K'],
    'F': ['G'],
    'G': ['A', 'C'],
    'H': ['B', 'K'],
    'K': ['B']
}


def algo_bfs(graphe, init, but):

    '''
    Implementation of the Breadth-First Search (BFS) algorithm to find the shortest path from a start node to a target node.
    Parameters:
       graphe: The graph to search through, represented as a dictionary of adjacency lists.
       init: The starting node for the search.
       but: The target node to find.
    Returns:
       The shortest path from init to but as a list, if one exists.
    '''
    closed = []  # List to keep track of visited nodes.
    l_open = [[init]]  # Queue of paths to be explored, starting with the path that only contains the start node.

    while l_open:  # Continue until there are no more paths to explore.
        
        print("closed =", closed)
        print("open =", l_open, "\n")
        
        chemin = l_open.pop(0)  # Dequeue the first path.
        noeud = chemin[-1]  # The current node to be explored is the last node in the path.

        if noeud in closed:  # Skip this node if it has already been visited.
            continue

        closed.append(noeud)  # Mark the current node as visited.

        if noeud == but:  # If the target node is found,
            return chemin  # return the path that led to it.

        # Explore adjacent nodes.
        noeuds_voisins = graphe.get(noeud, [])
        for noeud2 in noeuds_voisins:
            new_chemin = chemin.copy()  # Create a new path by extending the current path with the adjacent node.
            new_chemin.append(noeud2)
            l_open.append(new_chemin)  # Enqueue the new path for future exploration.
            
            if noeud2 == but:  # If an adjacent node is the target, return the path immediately.
                return new_chemin

# Execute the BFS algorithm to find the shortest path from node 'G' to node 'K'.
result = algo_bfs(graphe, 'G', 'K')
print("The shortest path is :", result)