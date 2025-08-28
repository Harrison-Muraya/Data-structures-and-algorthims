class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data 

    def __repr__(self):
        return "data in the node: %s" % self.data
    

class linked_list:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def size(self):

        count = 0
        current = self.head

        while current:
            count +=1
            current = current.next_node
        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def __repr__(self):

        node = []
        current = self.head

        while current:
            if current == self.head:
                node.append('head: %s' % current.data)
            elif current.next_node is None:
                node.append('tail: %s' % current.data)
            else:
                node.append('%s' % current.data)
            current = current.next_node
        return '->'.join(node)


l = linked_list()
l.add(11)
l.add(20)
l.add(90)
l.add(110)
print("Is Empty: ", l.isEmpty())
print("list size: ", l.size())
print(l)
