# Definition of the graph with nodes and their connections along with costs
graphe = {
    'E': [('X3', 7)],
    'A': [('B', 3), ('X1', 9)],
    'F': [('S', 1), ('C', 2), ('E', 2)],
    'C': [('X2', 5), ('S', 6), ('G', 7)],
    'S': [('A', 5), ('F', 6), ('B', 9)],
    'G': [('F', 2), ('X3', 8)],
    'X3': [],
    'B': [('C', 1), ('A', 2)],
    'X1': [],
    'X2': []
}

# Function to calculate the total cost of a path
def chemin_cout(chemin):

    """
    Calculates the total cost of a given path within the graph.
    
    Args:
    chemin: A list of tuples representing the path, where each tuple contains a node and the cost to reach that node.
    
    Returns:
    A tuple containing the total cost of the path and the current (last) node in the path. This function adds up
    the costs associated with each step in the path to provide a total cost for reaching the end node of the path.
    """

    total_cout = 0
    for (noeud, cout) in chemin:
        total_cout += cout
    return total_cout, chemin[-1][0]

# Uniform Cost Search Algorithm to find the lowest cost path to the goal
def ucs(graphe, init, but):

    """
    Performs the Uniform Cost Search algorithm to find the lowest cost path from an initial node to a goal node.
    
    Args:
    graphe: The graph where the search is to be performed, represented as a dictionary of adjacency lists with costs.
    init: The starting node for the search.
    but: The goal node to be reached.
    
    Returns:
    The path from the initial node to the goal node with the lowest total cost, as a list of tuples (node, cost).
    The function maintains a list of unexplored paths (l_open) and a list of explored nodes (closed). Paths in l_open
    are expanded in order of their cumulative cost from lowest to highest, ensuring the search favors the most
    cost-efficient paths first. Each iteration, the current path is expanded by exploring adjacent nodes and generating
    new paths with updated costs.
    """

    closed = []  # List of explored nodes
    l_open = [[(init, 0)]]  # Priority queue of paths to be explored, starting with the initial node

    while l_open:
        
        print("closed =", closed)
        print("open =", l_open, "\n")
        
        l_open.sort(key=chemin_cout)  # Sort paths by total cost, lowest first
        chemin = l_open.pop(0)  # Choose the path with the lowest cost
        noeud = chemin[-1][0]  # Current node to explore

        if noeud in closed:  # Skip explored nodes
            continue
        closed.append(noeud)
        
        if noeud == but:  # Goal reached
            return chemin
        
        # Explore neighbors
        noeuds_voisins = graphe.get(noeud, [])
        for (noeud2, cout) in noeuds_voisins:
            new_chemin = chemin.copy()
            new_chemin.append((noeud2, cout))
            l_open.append(new_chemin)

# Test the UCS algorithm to find the lowest cost path from 'S' to 'X3'
solution = ucs(graphe, 'S', 'X3')
print("The path of the lowest cost is : ", solution)
print("The cost of the solution is : ", chemin_cout(solution)[0])