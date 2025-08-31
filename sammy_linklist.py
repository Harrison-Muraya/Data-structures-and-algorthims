class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data


class Linked_list:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next_node
        
        return count
    
    def preappend(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next_nonde = self.head
            self.head = new_node
    
    def append(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            last = self.head

            while last.next_node:
                last = last.next_node
            last.next_node = Node(data)
