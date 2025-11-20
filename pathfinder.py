from path import Path
from priority_queue import PriorityQueue

# Array index const
INDONESIA = 0
SINGAPORE = 1
MALAYSIA = 2
THAILAND = 3
VIETNAM = 4
PHILLIPINES = 5
MYANMAR = 6
LAOS = 7
TAIWAN = 8
CHINA = 9

idx_to_country = {
    INDONESIA: "Indonesia",
    SINGAPORE: "Singapore",
    MALAYSIA: "Malaysia",
    THAILAND: "Thailand",
    VIETNAM: "Vietnam",
    PHILLIPINES: "Phillipines",
    MYANMAR: "Myanmar",
    LAOS: "Laos",
    TAIWAN: "Taiwan",
    CHINA: "China"
}

# Adjacency matrix with costs
cost_matrix = [
    [-1, 30, 35, -1, -1, 48, -1, -1, -1, -1],  # Indonesia
    [30, -1, -1, 21, -1, -1, -1, -1, -1, -1],  # Singapore
    [35, -1, -1, 16, 24, -1, -1, -1, -1, -1],  # Malaysia
    [-1, 21, 16, -1, -1, -1, 12, 9, -1, -1],   # Thailand
    [-1, -1, 24, -1, -1, -1, -1, -1, -1, 33],  # Vietnam
    [48, -1, -1, -1, -1, -1, -1, -1, 50, -1],  # Phillippines
    [-1, -1, -1, 12, -1, -1, -1, -1, -1, 15],  # Myanmar
    [-1, -1, -1, 9, -1, -1,  -1, -1, -1, 12],  # Laos
    [-1, -1, -1, -1, -1, 50, -1, -1, -1, -1],  # Taiwan
    [-1, -1, -1, -1, -1, -1, 15, 12, -1, -1]   # China
]


heuristic = {
    INDONESIA: 50,
    SINGAPORE: 40,
    MALAYSIA: 35,
    THAILAND: 30,
    VIETNAM: 32,
    PHILLIPINES: 27,
    MYANMAR: 13,
    LAOS: 18,
    TAIWAN: 15,
    CHINA: 0
}


def find_path(start, goal):
    priority_q = PriorityQueue()
    priority_q.put(Path(None, start, [], 0, heuristic[start]))
    while not priority_q.empty():
        priority_q.print_queue(idx_to_country)
        path = priority_q.get_top_and_pop()
        print("ACTION: Exploring the next path from the queue:", path.details(idx_to_country))
        
        if path.destination == goal:
            print("\n")
            print("GOAL FOUND!")
            print(path.details(idx_to_country))
            return
        
        neighbors = expand_neighbors(path.destination)

        for node, cost in neighbors:
            priority_q.put(Path(path.destination, node, path.visited_nodes, path.actual_cost + cost, heuristic[node]))
            
        print("\n")
    
def expand_neighbors(node):
    neighbors = []
    for neighbor, cost in enumerate(cost_matrix[node]):
        if cost != -1:
            neighbors.append((neighbor, cost))
    return neighbors
    
find_path(INDONESIA, CHINA)

