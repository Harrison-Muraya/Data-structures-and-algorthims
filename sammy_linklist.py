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
    
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            last = self.head

            while last.next_node:
                last = last.next_node
            last.next_node = Node(data)
    
    def prepend(self, data):
        first_node = Node(data)
        first_node.next_node = self.head
        self.head = first_node
    
   
    def __repr__(self):

        node = []
        current = self.head

        while current:
            if current == self.head:
                node.append('[head: %s]' % current.data)
            elif current.next_node is None:
                node.append('[tail: %s]' % current.data)
            else:
                node.append('[%s]' % current.data)
            current = current.next_node
        return '->'.join(node)



l = Linked_list()
l.append(11)
l.append(20)
l.append(90)
l.append(110)
print("Is Empty: ", l.isEmpty())
print("list size: ", l.size())
print("befor append:", l)
l.append(200)
print("after append:", l)
l.prepend(300)
print("after prepend", l)
