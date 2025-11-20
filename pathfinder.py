from path import Path
from priority_queue import PriorityQueue

# Array index
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

# Adjacency matrix with costs
cost_matrix = [
    [-1, 10, 15, -1, -1, -1, -1, -1, -1, -1],  # Indonesia
    [10, -1, 5, 20, -1, -1, -1, -1, -1, -1],  # Singapore
    [15, 5, -1, 10, 25, -1, -1, -1, -1, -1],  # Malaysia
    [-1, 20, 10, -1, 15, 30, -1, -1, -1, -1],  # Thailand
    [-1, -1, 25, 15, -1, 10, -1, 20, -1, -1],  # Vietnam
    [-1, -1, -1, 30, 10, -1, 5, -1, -1, -1],  # Phillippines
    [-1, -1, -1, -1, -1, 5, -1, 10, 15, -1],  # Myanmar
    [-1, -1, -1, -1, 20, -1, 10, -1, 5, -1],  # Laos
    [-1, -1, -1, -1, -1, -1, -1, 5, -1, 10],  # Taiwan
    [-1, -1, -1, -1, -1, -1, -1, -1, 10, -1]   # China
]


priority_q = PriorityQueue()

