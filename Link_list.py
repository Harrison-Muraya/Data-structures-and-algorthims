
class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "node data is: %s" % self.data

class Link_list:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None  
    
    def size(self):
        current = self.head
        count = 0

        while current:
            count +=1
        
        return count


    
n1 =Node(10)
print(n1)

n2 = Node(20)
n1.next_node=n2

print(n1.next_node)
