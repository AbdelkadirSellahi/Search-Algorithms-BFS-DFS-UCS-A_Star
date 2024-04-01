# Definition of the graph as a dictionary where each key is a node and its value is a list of adjacent nodes
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
    The Breadth-First Search (BFS) algorithm function
    Parameters:
       graphe: The graph on which the BFS is to be performed, represented as a dictionary
       init: The starting node for the BFS
       but: The target node that the algorithm aims to reach
    Returns:
       The shortest path from init to but as a list if such a path exists, else None
    '''   
    closed = []  # List to keep track of visited nodes
    l_open = [[init]]  # List of paths to be explored, starts with path containing only the starting node

    while l_open:  # Loop until there are no more paths to explore
        print("closed =", closed)
        print("open =", l_open, "\n")
        chemin = l_open.pop(0)  # Dequeue the first path
        noeud = chemin[-1]  # The current node to be explored is the last node in the path
        if noeud in closed:  # Skip this node if it has already been visited
            continue
        closed.append(noeud)  # Mark the current node as visited
        if noeud == but:  # Check if the target node has been reached
            return chemin  # Return the path leading to the target node
        else:  # If the target node has not been reached
            noeuds_voisins = graphe.get(noeud, [])  # Get the adjacent nodes of the current node
            for noeud2 in noeuds_voisins:  # For each adjacent node
                new_chemin = chemin.copy()  # Create a new path by copying the current path
                new_chemin.append(noeud2)  # Append the adjacent node to the new path
                l_open.append(new_chemin)  # Enqueue the new path for further exploration

# Test the BFS algorithm to find the shortest path from 'G' to 'K'
result = algo_bfs(graphe, 'G', 'K')
print("The shortest path is :", result)