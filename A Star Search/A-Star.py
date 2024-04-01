# Definition of the graph with nodes and their connections along with costs
graphe = {
    'Mila': [('Const', 3), ('Beja', 4), ('Jijel', 2)],
    'Const': [('Setif', 7)],
    'Beja': [('Boui', 2)],
    'Jijel': [('Beja', 1), ('Boui', 1)],
    'Setif': [('Alger', 4)],
    'Boui': [('Alger', 4)],
    'Alger': []
}

# Heuristic estimates to the goal for each node
estim = {
    'Mila': 9,
    'Const': 2,
    'Beja': 2,
    'Jijel': 5,
    'Setif': 2,
    'Boui': 3,
    'Alger': 0
}

# Function to calculate the total cost (f) of a path using the sum of actual costs (g) and heuristic (h)
def chemin_cout(chemin):

    """
    Calculates the total cost (f) for a given path. This total cost is the sum of the actual path cost (g)
    and the heuristic estimate to the goal (h).
    
    Args:
    chemin: A list of tuples representing the path, where each tuple contains a node and the cost to reach that node.
    
    Returns:
    A tuple containing the total cost of the path (f = g + h) and the current (last) node in the path.
    This function iterates over each step in the path to sum up the actual costs (g) and then adds the heuristic
    cost (h) from the last node to the goal.
    """
    
    cout_g = 0  # Actual cost to reach the current node
    for (noeud, cout) in chemin:
        cout_g += cout
    noeud_fils = chemin[-1][0]  # The last node in the path
    cout_h = estim[noeud_fils]  # Heuristic cost from the last node to the goal
    cout_f = cout_g + cout_h  # Total cost (f = g + h)
    return cout_f, noeud_fils

# A* Search Algorithm to find the shortest path to the goal
def a_star(graphe, init, but):

    """
    Performs the A* search algorithm to find the shortest path from an initial node to a goal node using both
    actual path costs and heuristic estimates.
    
    Args:
    graphe: The graph where the search is to be performed, represented as a dictionary of adjacency lists with costs.
    init: The starting node for the search.
    but: The goal node to be reached.
    
    Returns:
    The shortest path from the initial node to the goal node, as a list of tuples (node, cost). This function
    maintains a list of unexplored paths (l_open) and a list of explored nodes (closed). Paths in l_open are
    expanded based on their total cost (f = g + h) from lowest to highest, ensuring the search efficiently
    progresses towards the goal.
    """

    closed = []  # List of explored nodes
    l_open = [[(init, 0)]]  # List of paths to be explored, starting with the initial node

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

# Test the A* algorithm to find the shortest path from 'Mila' to 'Alger'
solution = a_star(graphe, 'Mila', 'Alger')
print("The shortest path from 'Mila' to 'Alger' is ", solution)
print("The total cost of the solution is ", chemin_cout(solution)[0])