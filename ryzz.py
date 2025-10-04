
class Node:
    next_node = None

    def __init__(self, data):
        self.data = data

class Linked_list:
    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    
    def isEmpty(self):
        return self.head == None
    
    def preappend(self, data): 
        if self.isEmpty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node


    def append(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            current = self.head
            while current.next_node:
                current = current.next_node            
            current.next_node = Node(data)


    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current == self.head:
                nodes.append('[head: %s]' % current.data)
            elif current.next_node == None:
                nodes.append('[tail: %s]' % current.data)
            else:
                nodes.append('[%s]' % current.data)
            current = current.next_node
        return '->'.join(nodes)
    
l = Linked_list()
print(l.isEmpty())
# print(l.search(90))
l.preappend(10)
l.preappend(30)
l.preappend(40)
l.preappend(150)
l.preappend(106)
print(l.isEmpty())
print(l)