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

# Function to calculate the total cost of a path and log the cost and current node
def chemin_cout(chemin):

    """
    Calculates the total cost of a given path and logs the cost and the current node.
    
    Args:
    chemin: A list of tuples representing the path, where each tuple is (node, cost).
    
    Returns:
    A tuple containing the total cost of the path and the last node in the path.
    This function iterates over each node in the path, summing the costs. When it reaches the
    last node, it prints the total cost and the current (last) node's name for logging purposes.
    """
    total_cout = 0
    for i, (noeud, cout) in enumerate(chemin):
        total_cout += cout
        if i == len(chemin) - 1:  # Print only for the last node in the path
            print("total_cost =", total_cout, "noued =", chemin[-1][0])
    return total_cout, chemin[-1][0]

# Uniform Cost Search Algorithm to find the lowest cost path to the goal
def ucs(graphe, init, but):

    """
    Implements the Uniform Cost Search algorithm to find the lowest cost path from an initial node to a goal node.
    
    Args:
    graphe: The graph represented as a dictionary where keys are node names, and values are lists of tuples
            (adjacent_node, cost).
    init: The starting node of the search.
    but: The target or goal node of the search.
    
    Returns:
    The path from the initial node to the goal node with the lowest total cost as a list of tuples (node, cost).
    This function maintains a priority queue (l_open) of paths, initialized with the starting node. It iterates
    over the queue, selecting the path with the lowest total cost for expansion. Nodes visited are added to a
    'closed' list to prevent revisiting. For each current node, it explores all adjacent nodes, creating new paths
    with updated costs, and adds these paths back into the priority queue for potential exploration.
    """

    closed = []  # List of explored nodes
    l_open = [[(init, 0)]]  # Priority queue of paths to be explored, starting with the initial node
    i = 0

    while l_open:
        
        i += 1
        print("Step =", i, "  ------------------------------------------")
        print("l_open Before sorting =", l_open)
        l_open.sort(key=chemin_cout)  # Sort paths by total cost, lowest first
        print("l_open After sorting =", l_open, "\n")
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

# Test the UCS algorithm to find the lowest cost path from 'S' to 'X2'
solution = ucs(graphe, 'S', 'X2')
print("The path of the lowest cost is : ", solution)
print("Cost of the solution is : ", chemin_cout(solution)[0])