
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
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count
    
    def peappend(self, data):
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
            new_node = Node(data)
            last = self.head

            while last.next_node is not None:
                last = last.next_node

            last.next_node = new_node

    def search(self, value):
        if self.isEmpty():
            return "linked list is Empty"
        else:
            current = self.head
            found = False

            while current:
                if current.data == value:
                    return True
                else:
                    current = current.next_node
            return False


    
    def __repr__(self):

        result = []
        current = self.head

        while current:
            if current == self.head:
                result.append('[head: %s]' % current.data)
            
            elif current.next_node is None:
                result.append('[tail: %s]' % current.data)
            
            else:
                result.append('[%s]' % current.data)
            current = current.next_node
        return '->'.join(result)

l = Linked_list()

print(f"is Empty: {l.isEmpty()}")
print(f"size: {l.size()}")
l.peappend(10)
l.peappend(16)
l.peappend(57)
l.peappend(100)
l.append(120)
print(f"is Empty: {l.isEmpty()}")
print(f"size: {l.size()}")
print(l)
print(f"search: {l.search(57)}")
print(f"search: {l.search(77)}")