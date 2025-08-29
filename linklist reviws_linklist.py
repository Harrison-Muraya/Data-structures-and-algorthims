class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

class LinkedList:
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
            new_node.next_node = self.head
            self.head = new_node
    
    def append(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            last = self.head

            while last.next_node:
                last = last.next_node            
            last.next_node = Node(data)

    def search(self, value):
        if self.isEmpty():
            return "linklist is Empty"
        else:
            current = self.head

            while current:
                if current.data == value:
                    return True
                else: 
                    current = current.next_node
            return None

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current == self.head:
                nodes.append('[head: %s]' % current.data)
            elif current.next_node is None:
                nodes.append('[tail: %s]' % current.data)
            else:
                nodes.append('[%s]' % current.data)
            current = current.next_node
        return '->'.join(nodes)
    
l = LinkedList()
print(l.isEmpty())
print(l.search(90))
l.preappend(10)
l.preappend(30)
l.preappend(40)
l.preappend(150)
l.preappend(106)
print(l.isEmpty())
print(f"after Preappending: {l.size()} {l}")
l.append(90)
print(f"after appending: {l.size()} {l}")
l.append(890)
print(f"after appending: {l.size()} {l}")
l.append(900)
print(f"after appending: {l.size()} {l}")

print(l.search(90))
print(l.search(9000))



