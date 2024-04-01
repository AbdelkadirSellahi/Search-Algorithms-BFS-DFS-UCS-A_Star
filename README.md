# Search Algorithms in Python

This repository contains implementations of various search algorithms in Python, intended for educational purposes. These algorithms demonstrate different strategies for traversing or searching through graphs to find paths between nodes, including Breadth-First Search (BFS), Depth-First Search (DFS), Uniform Cost Search (UCS), and A* Search.

## Introduction

Search algorithms are fundamental to the field of computer science, providing the backbone for pathfinding, puzzle solving, and optimization problems. This repository focuses on four key algorithms, each with its unique approach and application scenarios:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Uniform Cost Search (UCS)**
- **A-Star Search**

## Algorithms Detailed Overview

### Breadth-First Search (BFS)

BFS explores the graph layer by layer, ensuring the shortest path is found in an unweighted graph. It's particularly useful in scenarios like shortest path finding in unweighted graphs and solving puzzles with a minimal number of moves.

**Implementation Highlights**:
- BFS is implemented using a queue to maintain a list of yet-to-be-explored nodes.
- The algorithm systematically explores all neighbors of a node before moving on to the next level.

### Depth-First Search (DFS)

DFS dives deep into each branch before exploring neighbors, making it useful for applications that require visiting every node, such as cycle detection in graphs or puzzle solving where all solutions need to be enumerated.

**Implementation Highlights**:
- DFS uses a stack (implicitly via recursion or explicitly) to keep track of the exploration path.
- This approach is well-suited for exploring all possible paths or configurations in depth.

### Uniform Cost Search (UCS)

UCS expands on BFS by incorporating path costs, ensuring the lowest-cost path is selected first. It's optimal for finding the cheapest path in weighted graphs, like road networks or weighted puzzles.

**Implementation Highlights**:
- Implements a priority queue to manage the exploration of paths, prioritizing lower-cost paths.
- Each node expansion considers the cumulative cost from the start node, ensuring optimality.

### A* Search

A* Search combines UCS's cost-effectiveness with heuristics to efficiently find the lowest-cost path. It's best for weighted graphs where heuristic estimates to the goal are available, significantly speeding up search in large or complex graphs.

**Implementation Highlights**:
- Utilizes both actual path costs and heuristic estimates to prioritize path exploration.
- A* is particularly effective in applications like GPS navigation, where heuristic estimates can significantly reduce the search space.

## Comparison

This section outlines the practical applications, advantages, and limitations of each algorithm, providing insights into their optimal use cases.

The following table compares the algorithms based on their optimality, complexity, and usage scenarios:

| Algorithm | Optimality | Complexity | Usage Scenario |
|-----------|------------|------------|----------------|
| BFS       | Yes (unweighted) | O(b^d) | Unweighted graphs |
| DFS       | No | O(b^m) | Exploring all paths |
| UCS       | Yes | O(b^d) | Weighted graphs |
| A*        | Yes | O(b^d) | Weighted graphs with heuristics |

- `b` represents the branching factor of the graph.
- `d` represents the depth of the shortest path.
- `m` represents the maximum depth of the graph.

## Educational Purpose

This repository serves as an educational resource for understanding and comparing different search algorithms. Each algorithm is implemented in a clear and concise manner, suitable for educational purposes and algorithmic study.

## Running the Code

To run the algorithms:

1. Ensure you have Python 3.x installed on your machine.
2. Clone this repository to your local machine.
3. Navigate to the repository directory.
4. Run the desired algorithm using Python:
To run any of the algorithms, use Python 3:

```bash
python <algorithm_file>.py
```

Replace `<algorithm_file>` with the name of the algorithm you wish to run (e.g., `BFS-V1.py`).

## Contributions

Contributions to improve the implementations or documentation are welcome.

## Authors
- [**ABDELKADIR Sellahi**](https://github.com/AbdelkadirSellahi)
