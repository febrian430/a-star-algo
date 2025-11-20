class Path:
    def __init__(self, source, destination, previous_nodes, actual_cost, heuristic):
        self.visited_nodes = previous_nodes + [destination]
        self.source = source
        self.destination = destination
        self.actual_cost = actual_cost
        self.cost = actual_cost + heuristic

    def details(self, idx_to_country):
        return f"{self.stringify_visited_nodes(idx_to_country)} with estimated cost to goal {self.cost} (cost so far: {self.actual_cost})"
    
    def stringify_visited_nodes(self, idx_to_country):
        return " -> ".join(str(idx_to_country[node]) for node in self.visited_nodes)
        