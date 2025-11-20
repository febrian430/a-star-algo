from path import Path

class PriorityQueue:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def empty(self) -> bool:
        return self.head is None
    
    def put(self, path: Path):
        new_node = Node(path)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        elif self.head.path.cost > path.cost:
            new_node.next = self.head
            self.head = new_node
        elif self.tail.path.cost <= path.cost:
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            curr = self.head
            while curr.next is not None and curr.next.path.cost <= path.cost:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        

    def get_top_and_pop(self):
        if self.head is None:
            return None
        top_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return top_node.path
       
    def print_queue(self, idx_to_country):
        curr = self.head
        
        print("=============== Current Queue ================")
        while curr is not None:
            print(curr.path.details(idx_to_country))
            curr = curr.next
            
        print("=============================================")
    
class Node:
    def __init__(self, path: Path):
        self.path = path
        self.next = None